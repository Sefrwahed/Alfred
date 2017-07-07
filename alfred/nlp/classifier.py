from PyQt5.QtCore import QThread

import json
import os
import pickle

import numpy as np
from nltk import WordNetLemmatizer
from nltk import pos_tag
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

from alfred import alfred_globals as ag
from alfred.logger import Logger
from alfred.modules.module_info import ModuleInfo
from alfred.utils import Singleton


class Classifier(metaclass=Singleton):
    NO_MODULE = 0

    def __init__(self):
        self.train_thread = TrainingThread()

    def train(self):
        if self.train_thread.isRunning():
            self.train_thread.terminate()
            del self.train_thread

        self.train_thread = TrainingThread()
        if not self.train_thread.isRunning():
            self.train_thread.start()

    def predict(self, sent):
        module_id = self.train_thread.classifier.predict([sent])[0]
        Logger().info("Predicted module with id {}".format(module_id))
        return module_id


class PseudoClassifier:
    def __init__(self, target):
        self._target = target
        self.classes_ = [self._target]

    def predict(self, sentences):
        return [self._target for s in sentences]

    def predict_proba(self, sentences):
        return [[1] for s in sentences]


def identity(x):
    return x


class Preprocessor(BaseEstimator, TransformerMixin):
    def __init__(self, lowercase=True, remove_stopwords=True):
        self.lowercase = lowercase
        self.remove_stopwords = remove_stopwords

        self.stopwords = None
        self.lemmatizer = WordNetLemmatizer()

        if remove_stopwords:
            self.stopwords = set(stopwords.words(fileids=['english']))

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return list(map(self.tokenize, X))

    def tokenize(self, sent):
        tokens = word_tokenize(sent)
        pos = pos_tag(tokens)
        pos = filter(lambda p: p[1] != '.', pos)
        tokens = map(lambda p: self.lemmatize(p[0], p[1]), pos)
        if self.remove_stopwords:
            tokens = filter(lambda t: t not in self.stopwords, tokens)
        if self.lowercase:
            tokens = map(lambda t: t.lower(), tokens)
        return list(tokens)

    def lemmatize(self, token, pos_tag):
        pos_to_wn = {'N': wn.NOUN, 'V': wn.VERB, 'R': wn.ADV, 'J': wn.ADJ}
        wn_tag = wn.NOUN
        if pos_tag[0] in pos_to_wn:
            wn_tag = pos_to_wn[pos_tag[0]]

        return self.lemmatizer.lemmatize(token, wn_tag)

class TrainingThread(QThread):
    classifier = None
    clf_path = os.path.join(ag.user_folder_path, ag.clf_file)
    
    def __init__(self):
        QThread.__init__(self)
        if os.path.exists(self.clf_path):
            self.classifier = pickle.load(open(self.clf_path, "rb"))
        else:
            self.start()

    def _collect_dataset(self):
        all_info = ModuleInfo.all()
        sentences = []
        targets = []
        for mi in all_info:
            with open(mi.training_sentences_json_file_path()) as train_file:
                m_sent = json.load(train_file)

                sentences.extend(m_sent)
                targets.extend(len(m_sent) * [mi.id])
                
            if os.path.exists(mi.extra_training_sentences_json_file_path()):
                with open(mi.extra_training_sentences_json_file_path()) as train_file:
                    m_sent = json.load(train_file)

                    sentences.extend(m_sent)
                    targets.extend(len(m_sent) * [mi.id])

        return sentences, targets

    def run(self):
        Logger().info("Training started")

        sentences, targets = self._collect_dataset()

        n_targets = len(set(targets))
        if n_targets < 2:
            target = Classifier.NO_MODULE if n_targets == 0 else targets[0]
            self.classifier = PseudoClassifier(target)
            Logger().info('No training needed for less than 2 modules')
        else:
            preprocessor = Preprocessor(remove_stopwords=True)
            vectorizer = TfidfVectorizer(tokenizer=identity,
                                         lowercase=False,
                                         preprocessor=None)
            clf = SVC(kernel='linear', probability=True)
            pipeline = Pipeline([
                ('preprocessor', preprocessor),
                ('vectorizer', vectorizer),
                ('clf', clf),
            ])

            params = {
                'preprocessor__lowercase': [True, False],
                'vectorizer__ngram_range': [(1, n) for n in range(1, 4)],
                'clf__C': np.logspace(-3, 0, 20),
                'clf__gamma': np.logspace(-3, 1, 4),
            }

            grid_search = GridSearchCV(pipeline, params, n_jobs=-1, verbose=1)
            grid_search.fit(sentences, targets)

            error = 1 - grid_search.best_score_
            Logger().info('Training Error = {err:0.2f}'.format(err=error * 100))
            Logger().info('Best parameters: ' + str(grid_search.best_params_))

            self.classifier = grid_search.best_estimator_

        pickle.dump(self.classifier, open(self.clf_path, "wb"))
        Logger().info("Training ended")