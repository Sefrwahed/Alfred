import os
import pickle
import json

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from alfred import alfred_globals as ag
from alfred.lib import Singleton
from alfred.logger import Logger
from alfred.modules.module_info import ModuleInfo


class Classifier(metaclass=Singleton):
    def __init__(self):
        self.clf_path = os.path.join(ag.user_folder_path, ag.clf_file)

        if os.path.exists(self.clf_path):
            self.classifier = pickle.load(open(self.clf_path, "rb"))
        else:
            self.train()

    def train(self):
        Logger().info("Training started")

        all_info = ModuleInfo.all()
        self.classifier = Pipeline([
            ('vect', CountVectorizer(
                analyzer='word', stop_words='english', ngram_range=(1, 3)
            )),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB())
        ])

        sentences = []
        targets = []

        for mi in all_info:
            with open(mi.training_sentences_json_file_path()) as train_file:
                m_sent = json.load(train_file)

                sentences.extend(m_sent)
                targets.extend(len(m_sent) * [mi.id])

        if sentences:
            self.classifier.fit(sentences, targets)
            pickle.dump(self.classifier, open(self.clf_path, "wb"))

        Logger().info("Training ended")

    def predict(self, sent):
        if ModuleInfo.all():
            module_id = self.classifier.predict([sent])[0]
            Logger().info("Predicted module with id {}".format(module_id))
            return module_id
        else:
            return 0
