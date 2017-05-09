from abc import ABC

import dataset

import alfred.modules.api.a_module_globals as amg


class ABaseModel(ABC):
    database = None

    def __init__(self):
        ABaseModel.database = dataset.connect(f'sqlite:///{amg.module_db_path}')
        self._id = None

    @property
    def id(self):
        return self._id

    def save(self):
        ABaseModel.database = dataset.connect(f'sqlite:///{amg.module_db_path}')
        objects = ABaseModel.database[self.__class__.__name__]

        data_dict = self.__dict__.copy()
        exists = objects.find_one(id=self._id)

        if exists:
            data_dict['id'] = data_dict['_id']
        del data_dict['_id']

        if not exists:
            self._id = objects.insert(data_dict)  # new record
        else:
            objects.update(data_dict, ['id'])  # update record

        ABaseModel.database.commit()

    def delete(self):
        ABaseModel.database = dataset.connect(f'sqlite:///{amg.module_db_path}')
        ABaseModel.database[self.__class__.__name__].delete(id=self._id)
        ABaseModel.database.commit()

    @classmethod
    def find_by(cls, **kwargs):
        cls.database = dataset.connect(f'sqlite:///{amg.module_db_path}')

        dataset_dict = cls.database[cls.__name__].find_one(**kwargs)
        model = cls.__populate_model(dataset_dict)

        del cls.database
        return model

    @classmethod
    def find(cls, id):
        return cls.find_by(id=id)

    @classmethod
    def all(cls):
        cls.database = dataset.connect(f'sqlite:///{amg.module_db_path}')

        models = []
        for d in cls.database[cls.__name__].all():
            model = cls.__populate_model(d)
            models.append(model)

        del cls.database
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
