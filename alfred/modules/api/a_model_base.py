from abc import ABC
import dataset

db = dataset.connect('sqlite:///db')


class AModelBase(ABC):
    def __init__(self):
        self.id = None

    def save(self):
        objects = db[type(self).__name__]
        if objects.find_one(id=self.id):
            objects.update(self.__dict__, ['id'])
        else:
            self.id = objects.insert(self.__dict__)

    @classmethod
    def find(cls, id):
        model = cls()
        model.__dict__ = db[cls.__name__].find_one(id=id)
        return model

    @classmethod
    def all(cls):
        objects = []
        for m in db[cls.__name__].all():
            obj = cls()
            obj.__dict__ = m
            objects.append(obj)
        return objects
