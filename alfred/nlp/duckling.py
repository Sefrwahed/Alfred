from alfred.utils import Singleton
from .ner import NER

from duckling import DucklingWrapper


class Duckling(NER, metaclass=Singleton):

    def __init__(self):
        self.ducklingInstance = DucklingWrapper()

    def getNER(self, entities_type_list, text):
        entities = []
        for dimType in entities_type_list:
            method_name = "parse_" + dimType
            entity = getattr(self.ducklingInstance, method_name)(text)
            print(entity)
            entities.append(entity)

        return entities

    def getNameEntities(self, entities_types_list, text):
        entities = self.getNER(entities_types_list, text)
        return {entity[0]["dim"]: entity[0]["value"]["value"]
                for entity in entities}



