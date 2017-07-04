from abc import ABCMeta
from abc import abstractmethod


class NER(metaclass=ABCMeta):
    @abstractmethod
    def set_entities_types(self, entities_types):
        """
        self.entities_types_list = entities_types
        """

    @abstractmethod
    def get_ner(self, text):
        """
        Get the entities extracted either from spacy or duckling
        """

    @abstractmethod
    def get_name_entities(self, text):
        """
        parse the entities extracted either from spacy or duckling and return it
        """