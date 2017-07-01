import json
import os
import re
import numpy as np
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from alfred import alfred_globals as ag
from alfred.modules.db_manager import DBManager


class ModuleInfo(DBManager().DBModelBase):
    __tablename__ = 'module_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    source = Column(String(256), nullable=False)
    user = Column(String(256), nullable=False)
    version = Column(String(256), nullable=False)

    def __init__(self, name, source, user, version):
        self.name = name
        self.source = source
        self.user = user
        self.version = version
        DBManager().refresh_tables()

    def root(self):
        return os.path.join(ag.modules_folder_path,
                            self.source,
                            self.user,
                            self.name)

    def training_sentences_json_file_path(self):
        return os.path.join(self.root(),
                            self.package_name(),
                            'resources',
                            'training_sentences.json')

    def needed_entities(self):
        path =  os.path.join(self.root(),
                            self.package_name(),
                            'resources',
                            'needed_entities.json')
        with open(path) as entities_file:
            entities_sent = json.load(entities_file)


        return entities_sent


    def package_name(self) -> str:
        return re.sub(r'\W', '_', self.name)

    def entry_point(self):
        return self.package_name() + ".py"

    def class_name(self):
        return "".join(w.title() for w in self.package_name().split("_"))

    def create(self):
        DBManager().session.add(self)
        DBManager().session.commit()

    def destroy(self):
        DBManager().session.query(ModuleInfo).filter(
            ModuleInfo.id == self.id
        ).delete()
        DBManager().session.commit()

    @classmethod
    def find_by_id(cls, module_id):
        return DBManager().session.query(ModuleInfo).get(int(module_id))

    @classmethod
    def get_needed_entities(cls, mod_id):
        res = DBManager().session.query(ModuleInfo, Entity).filter(ModuleInfo.id == mod_id)
        return res

    @classmethod
    def all(cls):
        return DBManager().session.query(ModuleInfo).all()


class Entity(DBManager().DBModelBase):
    __tablename__ = 'entity'

    entity_id = Column(Integer, primary_key=True, autoincrement=True)
    module_id = Column(Integer, ForeignKey(ModuleInfo.id), nullable=False)
    entity_name = Column(String(256), nullable=False)
    module_info = relationship("ModuleInfo", order_by=entity_id, back_populates="entities")

    DBManager().refresh_tables()

    def __init__(self, entity_name):
        self.entity_name = entity_name

    def create(self):
        DBManager().session.add(self)
        DBManager().session.commit()

ModuleInfo.entities = relationship("Entity", back_populates="module_info")
DBManager().refresh_tables()
