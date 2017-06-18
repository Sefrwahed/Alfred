from alfred.utils import Singleton
from abc import abstractmethod


class NER(metaclass=Singleton):
    def __init__(self, entities_list, text):
        pass

    @abstractmethod
    def getNER(self, entities_types_list, text):
        """
        Get the entities extracted either from spacy or duckling
        """

    @abstractmethod
    def getNameEntities(self, entities_types_list, text):
        """
        parse the entities extracted either from spacy or duckling and return it
        """

