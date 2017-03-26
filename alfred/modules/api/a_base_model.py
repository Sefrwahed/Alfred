from abc import ABC

import dataset


class AbstractABaseModel(ABC):
    database = None

    @classmethod
    def connect(cls, database_path):
        cls.database = dataset.connect(f'sqlite:///{database_path}')

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
    def find_by(cls, **kwargs):
        model = cls.__new__(cls)
        dataset_dict = cls.database[cls.__name__].find_one(**kwargs)

        if dataset_dict is None:
            return None

        data_dict = dict(dataset_dict)

        data_dict['_id'] = data_dict['id']
        del data_dict['id']
        model.__dict__ = data_dict
        return model

    @classmethod
    def find(cls, id):
        return cls.find_by(id=id)

    @classmethod
    def all(cls):
        objects = []
        for m in cls.database[cls.__name__].all():
            obj = cls.__new__(cls)
            obj.__dict__ = m
            objects.append(obj)
        return objects

    @classmethod
    def delete(cls, model_id):
        return cls.database[cls.__name__].delete(id=model_id)
