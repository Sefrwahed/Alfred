import alfred.nlp.entity_type as entity
import alfred.nlp.ner_parsers as parsers
from alfred.utils import Singleton
from alfred.logger import Logger


class Parser(metaclass=Singleton):
    def __init__(self, entities):
        self.entities_list = entities
        self.duckling_list = entity.DucklingEntities
        self.spacy_list = entity.SpacyEnitites
        self.NERParser_list = []
        self.parsed_entities = []
        Logger().info("Instantiating Parsers..")
        self.nerObjects = {"Duckling": parsers.Duckling([]), "Spacy": parsers.Spacy()}
        Logger().info("Parsers are Instantiated ..")

    def set_entities_types(self, entities):
        self.entities_list = entities

    def parse(self, text):
        self.parsed_entities.clear()
        self.NERParser_list.clear()

        Logger().info("Parsing entities in progress..")
        self.parse_list(text)
        Logger().info("Finished parsing entities..")
        return self.parsed_entities

    def parse_list(self, text):
        spacy_entities_list = []
        duckling_entities_list = []

        for entity_name in self.entities_list:
            if entity_name in self.duckling_list:
                duckling_entities_list.append(entity_name)
            elif entity_name in self.spacy_list:
                spacy_entities_list.append(entity_name)

        Logger().info("Module's spacy list is {}".format(spacy_entities_list))
        Logger().info("Module's duckling list is {}".format(duckling_entities_list))

        if duckling_entities_list:
            self.nerObjects["Duckling"].set_entities_types(duckling_entities_list)
            self.NERParser_list.append(self.nerObjects["Duckling"])

        if spacy_entities_list:
            self.nerObjects["Spacy"].set_entities_types(spacy_entities_list)
            self.NERParser_list.append(self.nerObjects["Spacy"])

        if self.NERParser_list:
            for parser in self.NERParser_list:
                t_text = text
                while True:
                    named_entity = parser.get_name_entities(text)
                    for key in named_entity :
                        pass
                    self.parsed_entities.append()
                    if t_text == "" or named_entity:
                        break