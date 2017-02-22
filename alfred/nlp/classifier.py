import os
import pickle
import json

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from alfred import alfred_globals as ag
from alfred.modules import module_info


clf_path = os.path.join(ag.user_folder_path, ag.clf_file)
classifier = None


def train():
    all_info = module_info.get_all_module_info()
    global classifier
    classifier = Pipeline([
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

    classifier.fit(sentences, targets)
    pickle.dump(classifier, open(clf_path, "wb"))


def predict(sent):
    global classifier
    module_id = classifier.predict([sent])[0]
    return module_id

if os.path.exists(clf_path):
    classifier = pickle.load(open(clf_path, "rb"))
else:
    train()
