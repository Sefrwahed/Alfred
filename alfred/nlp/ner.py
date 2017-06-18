import spacy
from alfred.utils import Singleton
from duckling import DucklingWrapper

class NER(metaclass=Singleton):
    def __init__(self):
        self.spacyNlp = spacy.load('en', parser=None)
        self.ducklingInstance = DucklingWrapper()


    def getNERDuckling(self, text, dimType):
        method_name = "parse_"+ dimType
        entity = getattr(self.ducklingInstance, method_name)(text)
        self.getNameEntitiesDuck(entity)
        print(entity)
        return entity

    def getNameEntitiesDuck(self, entityList):
        dim = entityList[0]["dim"]
        value = entityList[0]["value"]["value"]

        print(dim, value)
        return {dim : value}

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