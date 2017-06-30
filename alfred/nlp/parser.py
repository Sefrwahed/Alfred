import alfred.nlp.entity_type as entity
import alfred.nlp.ner_parsers as parsers
from alfred.utils import Singleton
from alfred.logger import Logger


class Parser(metaclass=Singleton):
    def __init__(self, entities_list):
        self.entities_list = entities_list
        self.duckling_list = entity.DucklingEntities
        self.spacy_list = entity.SpacyEnitites
        self.NERParser_list = []
        self.parsed_entities = []
        self.nerObjects = {"Duckling": parsers.Duckling([]), "Spacy": parsers.Spacy()}

    def parse(self, text):
        Logger().info("Parsing entities in progress..")
        self.parse_list(text)
        Logger().info("Finished parsing entities..")
        return self.parsed_entities

    def parse_list(self, text):
        spacy_entities_list = []
        duckling_entities_list = []

        for entity_item in self.entities_list:
            entity = entity_item.entity_name
            if entity in self.duckling_list:
                duckling_entities_list.append(entity)
            elif entity in self.spacy_list:
                spacy_entities_list.append(entity)

        Logger().info("module spacy list is {}".format(spacy_entities_list))
        Logger().info("module duckling list is {}".format(duckling_entities_list))

        if duckling_entities_list:
<<<<<<< HEAD
            self.nerObjects["Duckling"].resetEntitiesTypes(duckling_entities_list)
            self.NERParser_list.append(self.nerObjects["Duckling"])

        if spacy_entities_list:
            self.nerObjects["Spacy"].resetEntitiesTypes(spacy_entities_list)
            self.NERParser_list.append(self.nerObjects["Spacy"])
=======
            duckling_parser = parsers.Duckling(duckling_entities_list)
            self.NERParser_list.append(duckling_parser)

        if spacy_entities_list:
            spacy_parser = parsers.Spacy(spacy_entities_list)
            self.NERParser_list.append(spacy_parser)

>>>>>>> ed61e1cbdc96153d3438bb4e5709c79431fd49ad

        if self.NERParser_list:
            for parser in self.NERParser_list:
                self.parsed_entities.append(parser.getNameEntities(text))

