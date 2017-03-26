from abc import ABC
import dataset


class ABaseModel(ABC):
    database = dataset.connect('sqlite:///db')

    def __init__(self):
        self._id = None

    @property
    def id(self):
        return self._id

    def save(self):
        cls = type(self)
        objects = cls.database[cls.__name__]

        data_dict = self.__dict__.copy()
        exists = objects.find_one(id=self._id)

        if exists:
            data_dict['id'] = data_dict['_id']
        del data_dict['_id']

        if not exists:
            self._id = objects.insert(data_dict)  # new record
        else:
            objects.update(data_dict, ['id'])  # update record

    @classmethod
    def find(cls, id):
        model = cls()
        data_dict = dict(cls.database[cls.__name__].find_one(id=id))

        if data_dict is None:
            return None

        del data_dict['id']
        model.__dict__ = data_dict
        model._id = id
        return model

    @classmethod
    def all(cls):
        objects = []
        for m in cls.database[cls.__name__].all():
            obj = cls()
            obj.__dict__ = m
            objects.append(obj)
        return objects
