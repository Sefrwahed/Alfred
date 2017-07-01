from duckling import DucklingWrapper
from alfred.nlp.ner_parsers.ner import NER
from alfred.logger import Logger


class Duckling(NER):

    def __init__(self, entities_types):
        self.entities_types_list = entities_types
        self.ducklingInstance = DucklingWrapper()

    def set_entities_types(self, entities_types):
        self.entities_types_list = entities_types

    def get_ner(self, text):
        pass

    def get_name_entities(self, text):
        entities = []
        for dimType in self.entities_types_list:
            method_name = "parse_" + dimType
            entity = getattr(self.ducklingInstance, method_name)(text)
            entities.append(entity)
        return {entity[0]["dim"]: [entity[0]["value"]["value"], entity[0]["text"]]
                for entity in entities}
