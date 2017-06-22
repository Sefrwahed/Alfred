import alfred.nlp.entity_type as entity
import alfred.nlp.ner_parsers as parsers
from alfred.utils import Singleton

class Parser(metaclass=Singleton)
    def __init__(self, entities_list):
        self.entities_list = entities_list
        self.duckling_list = entity.DucklingEntities
        self.spacy_list = entity.SpacyEnitites
        self.NERParser_list = []
        self.parsed_entities = []

    def parse(self, text):
        self.parse_list(text, self.entities_list)

    def parse_list(self, text, entities_list):
        spacy_entities_list = []
        duckling_entities_list = []

        for entity in entities_list:
            if entity in self.duckling_list:
                duckling_entities_list.append(entity)
            elif entity in self.spacy_list:
                spacy_entities_list.append(entity)

        if spacy_entities_list:
            self.NERParser_list.append(parsers.Spacy(spacy_entities_list))
        if duckling_entities_list:
            self.NERParser_list.append(parsers.Duckling(duckling_entities_list))

        if self.NERParser_list:
            for parser in self.NERParser_list:
                self.parsed_entities.append(parser.getNameEntities(text))