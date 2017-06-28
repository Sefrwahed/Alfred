import uuid

import os
import re
import numpy as np
from sqlalchemy import Column, Integer, String
from sqlalchemy import Text

from alfred import alfred_globals as ag
from alfred.modules.db_manager import DBManager


class ModuleInfo(DBManager().DBModelBase):
    __tablename__ = 'module_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    source = Column(String(256), nullable=False)
    user = Column(String(256), nullable=False)
    version = Column(String(256), nullable=False)
    entities = Column(Text(length=36), default=lambda: str(uuid.uuid4()))


    def __init__(self, name, source, user, version, entities = np.asarray(["time"])):
        self.name = name
        self.source = source
        self.user = user
        self.version = version
        self.entities = entities
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
    def find_by_id(cls, id):
        return DBManager().session.query(ModuleInfo).get(int(id))

    @classmethod
    def get_needed_entities(cls, id):
        return DBManager().session.query(ModuleInfo.entities).get(int(id))


    @classmethod
    def all(cls):
        return DBManager().session.query(ModuleInfo).all()


DBManager().refresh_tables()
