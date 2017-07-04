import alfred.nlp.entity_type as entity
import alfred.nlp.ner_parsers as parsers
from alfred.nlp.true_casing import AlfredTrueCasing as true_casing
from alfred.utils import Singleton
from alfred.logger import Logger


class Parser(metaclass=Singleton):
    def __init__(self, entities_list):
        self.entities_list = entities_list
        self.duckling_list = entity.DucklingEntities
        self.spacy_list = entity.SpacyEnitites
        self.NERParser_list = []
        self.parsed_entities = []
        self.true_casing = true_casing()
        Logger().info("Instantiating Parsers..")
        self.nerObjects = {"Duckling": parsers.Duckling([]), "Spacy": parsers.Spacy()}

    def parse(self, text):
        self.parsed_entities.clear()
        self.NERParser_list.clear()
        doc = self.nerObjects["Spacy"].spacyNlp(text)
        pos_tags = []
        for word in doc:
            pos_tags.append((str(word), str(word.tag_)))
        text = self.true_casing.fix(pos_tags)

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
                self.parsed_entities.append(parser.get_name_entities(text))
