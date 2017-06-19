import spacy

from alfred.nlp.ner_parsers.ner import NER
from alfred.utils import Singleton


class Spacy(NER, metaclass=Singleton):

    def __init__(self, entities_types):
        NER.__init__(entities_types)
        self.spacyNlp = spacy.load('en', parser=None)

    def getNER(self, text):
        doc = self.spacyNlp(text)
        entities = {}
        for ent in doc.ents:
            if ent.label_ in entities:
                entities[ent.label_].append(ent)
            else:
                entities[ent.label_] = [ent]
        return entities

    def getNameEntities(self, text):
        entities = self.getNER(text)
        return {entities_type: entities[entities_type]
                for entities_type in self.entities_types_list}