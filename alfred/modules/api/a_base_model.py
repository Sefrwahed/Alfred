from abc import ABC

import threading
import dataset

class ABaseModel(ABC):
    database = None
    db_path = ''

    @classmethod
    def db_path(cls, db_path):
        print("model connect", threading.get_ident())
        cls.db_path = db_path

    def __init__(self):
        self.database = dataset.connect(f'sqlite:///{self.db_path}')
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

    def delete(self):
        cls = self.__class__
        return cls.database[cls.__name__].delete(id=self._id)

    @classmethod
    def find_by(cls, **kwargs):
        dataset_dict = cls.database[cls.__name__].find_one(**kwargs)
        model = cls.__populate_model(dataset_dict)
        return model

    @classmethod
    def find(cls, id):
        return cls.find_by(id=id)

    @classmethod
    def all(cls):
        cls.database = dataset.connect(f'sqlite:///{cls.db_path}')
        models = []
        for d in cls.database[cls.__name__].all():
            model = cls.__populate_model(d)
            models.append(model)
        return models

    @classmethod
    def __populate_model(cls, dataset_dict):
        model = cls.__new__(cls)

        if dataset_dict is None:
            return None

        data_dict = dict(dataset_dict)

        data_dict['_id'] = data_dict['id']
        del data_dict['id']
        model.__dict__ = data_dict

        return model
