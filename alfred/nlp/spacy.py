from alfred.utils import Singleton
from .ner import NER

import spacy


class Spacy(NER, metaclass=Singleton):

    def __init__(self):
        self.spacyNlp = spacy.load('en', parser=None)

    def getNER(self, entities_types_list, text):
        doc = self.spacyNlp(text)
        entities = {}
        for ent in doc.ents:
            if ent.label_ in entities:
                entities[ent.label_].append(ent)
            else:
                entities[ent.label_] = [ent]
        return entities

    def getNameEntities(self, entities_types_list, text):
        entities = self.getNER(text)
        return {entities_type: entities[entities_type]
                for entities_type in entities_types_list}
