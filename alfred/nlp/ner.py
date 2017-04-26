from spacy.vocab import Vocab
from spacy.pipeline import EntityRecognizer
from spacy.tokens.doc import Doc

from alfred import alfred_globals as ag
from alfred.utils import Singleton


class NER(metaclass=Singleton):
    def __init__(self):
        self._spacyVocab = Vocab.load(path=ag.spacy_path,
                                      tag_map=ag.spacy_tag_map,
                                      oov_prob=-19.502029)
        self._spacyER = EntityRecognizer.load(path=ag.spacy_ner_path,
                                              vocab=self._spacyVocab,
                                              require=True)

    def make_doc(self, text):
        import jieba
        words = list(jieba.cut(text, cut_all=True))
        return Doc(self._spacyVocab, words=words, spaces=[False]*len(words))

    def spacyNER(self, sentence):
        doc = self.make_doc(sentence)
        self._spacyER.__call__(doc)
        return doc
