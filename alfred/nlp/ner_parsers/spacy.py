import spacy

from alfred.nlp.ner_parsers.ner import NER
from alfred.nlp.entity_type import SpacyEnitites


class Spacy(NER):
    def __init__(self, entities_types=SpacyEnitites):
        self.entities_types_list = entities_types
        self.spacyNlp = spacy.load('en', parser=None)

    def set_entities_types(self, entities_types):
        self.entities_types_list = entities_types

    def get_ner(self, text):
        doc = self.spacyNlp(text)
        entities = {}
        for ent in doc.ents:
            if ent.label_ in entities:
                entities[ent.label_].append(ent)
            else:
                entities[ent.label_] = [ent]
        return entities

    def get_name_entities(self, text):
        entities = self.get_ner(text)
        return {entities_type: [entities[entities_type], entities[entities_type]]
                for entities_type in self.entities_types_list}

    def getAnnotatedText(self, text):
        entities = self.get_ner(text)
        for type in entities:
            text = text.replace(str(entities[type][0]), type)
        return text
