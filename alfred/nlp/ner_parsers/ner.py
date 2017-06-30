from abc import ABCMeta
from abc import abstractmethod


class NER(metaclass=ABCMeta):
    @abstractmethod
    def resetEntitiesTypes(self, entities_types):
        """
        self.entities_types_list = entities_types
        """

    @abstractmethod
    def getNER(self, text):
        """
        Get the entities extracted either from spacy or duckling
        """

    @abstractmethod
    def getNameEntities(self, text):
        """
        parse the entities extracted either from spacy or duckling and return it
        """