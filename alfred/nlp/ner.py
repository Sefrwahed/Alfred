import spacy

from alfred import alfred_globals as ag
from alfred.utils import Singleton
from duckling import DucklingWrapper

class NER(metaclass=Singleton):
    def __init__(self):
        self.spacyNlp = spacy.load('en', parser=None)
        self.ducklingInstance = DucklingWrapper()


    def getNERDuckling(self, text):
        entities = self.ducklingInstance.parse_time(text)
        print(entities)
        return entities

    def getNERSpacy(self, text):
        doc = self.spacyNlp(text)
        entities = {}
        for ent in doc.ents:
            if ent.label_ in entities:
                entities[ent.label_].append(ent)
            else:
                entities[ent.label_] = [ent]
        return entities

    def getNameEntities(self, entities_types_list, text):
        entities = self.getNERSpacy(text)
        return {entities_type: entities[entities_type]
                for entities_type in entities_types_list}