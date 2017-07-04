import pickle
import sklearn_crfsuite


class AlfredTrueCasing:
    def __init__(self):
        self._model = pickle.load(open('alfred_truecasing.model', 'rb'))

    def word2features(self, doc, i):
        word = doc[i][0]
        postag = doc[i][1]

        features = [
            'bias',
            'word.lower=' + word.lower(),
            'word[-3:]=' + word[-3:],
            'word[-2:]=' + word[-2:],
            'word.isdigit=%s' % word.isdigit(),
            'postag=' + postag
        ]
        if i > 0:
            word1 = doc[i-1][0]
            postag1 = doc[i-1][1]
            features.extend([
                '-1:word.lower=' + word1.lower(),
                '-1:word.isdigit=%s' % word1.isdigit(),
                '-1:postag=' + postag1
            ])
        else:
            features.append('BOS')

        if i < len(doc)-1:
            word1 = doc[i+1][0]
            postag1 = doc[i+1][1]
            features.extend([
                '+1:word.lower=' + word1.lower(),
                '+1:word.isdigit=%s' % word1.isdigit(),
                '+1:postag=' + postag1
            ])
        else:
            features.append('EOS')

        return features

    def extract_features(self, doc):
        return [self.word2features(doc, i) for i in range(len(doc))]

    def fix(self, pos_tags):
        features = [self.extract_features(pos_tags)]
        casing = self._model.predict(features)[0]
        tokens = []
        for word in pos_tags:
            tokens.append(word[0])
        for i in range(len(casing)):
            if casing[i] == 'True':
                tokens[i] = tokens[i].title()
        return ' '.join(tokens)
