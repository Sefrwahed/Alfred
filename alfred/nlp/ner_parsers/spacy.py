import spacy

from alfred.nlp.ner_parsers.ner import NER
from alfred.nlp.entity_type import SpacyEnitites


class Spacy(NER):

<<<<<<< HEAD
    def __init__(self, entities_types=SpacyEnitites):
=======
    def __init__(self, entities_types = SpacyEnitites):
>>>>>>> ed61e1cbdc96153d3438bb4e5709c79431fd49ad
        self.entities_types_list = entities_types
        self.spacyNlp = spacy.load('en', parser=None)

    def resetEntitiesTypes(self, entities_types):
        self.entities_types_list = entities_types

    def getNER(self, text):
        doc = self.spacyNlp(text)
        entities = {}
        for ent in doc.ents:
            if ent.label_ in entities:
                entities[ent.label_].append(ent)
            else:
                entities[ent.label_] = [ent]
        return entities

    def getNameEntities(self, text):
        entities = self.getNER(text)
        return {entities_type: entities[entities_type]
                for entities_type in self.entities_types_list}

    def getAnnotatedText(self, text):
        entities = self.getNER(text)
        for type in entities:
            text = text.replace(str(entities[type][0]), type)
        return text
