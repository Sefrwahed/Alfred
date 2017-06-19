from duckling import DucklingWrapper

from alfred.nlp.ner_parsers.ner import NER
from alfred.utils import Singleton


class Duckling(NER, metaclass=Singleton):

    def __init__(self, entities_types):
        NER.__init__(self,entities_types)
        self.ducklingInstance = DucklingWrapper()

    def getNER(self, text):
        pass

    def getNameEntities(self, text):
        entities = []
        for dimType in self.entities_types_list:
            method_name = "parse_" + dimType
            entity = getattr(self.ducklingInstance, method_name)(text)
            print(entity)
            entities.append(entity)
        return {entity[0]["dim"]: entity[0]["value"]["value"]
                for entity in entities}