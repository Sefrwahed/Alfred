import json
import os
import re
from sqlalchemy import Column, Integer, String

from alfred import alfred_globals as ag
from alfred.modules.db_manager import DBManager


class ModuleInfo(DBManager().DBModelBase):
    __tablename__ = 'module_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    source = Column(String(256), nullable=False)
    user = Column(String(256), nullable=False)
    version = Column(String(256), nullable=False)

    def __init__(self, id, name, source, user, version):
        self.id = id
        self.name = name
        self.source = source
        self.user = user
        self.version = version

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

    def extra_training_sentences_json_file_path(self):
        return os.path.join(self.root(),
                            'data',
                            'extra_training_sentences.json')

    def needed_entities(self):
        path = os.path.join(self.root(),
                            self.package_name(),
                            'resources',
                            'needed_entities.json')
        if os.path.isfile(path):
            with open(path) as entities_file:
                needed_entities = json.load(entities_file)
        else:
            needed_entities = []

        return needed_entities

    def package_name(self) -> str:
        return re.sub(r'\W', '_', self.name)

    def entry_point(self):
        return self.package_name() + ".py"

    def class_name(self):
        return "".join(w.title() for w in self.package_name().split("_"))

    def create(self):
        session = DBManager().session()
        session.add(self)
        session.commit()
        session.close()

    def destroy(self):
        session = DBManager().session()
        session.query(ModuleInfo).filter(
            ModuleInfo.id == self.id
        ).delete()
        session.commit()
        session.close()

    @classmethod
    def find_by_id(cls, module_id):
        session = DBManager().session()
        mi = session.query(ModuleInfo).get(int(module_id))
        session.close()
        return mi

    @classmethod
    def all(cls):
        session = DBManager().session()
        all_info = session.query(ModuleInfo).all()
        session.close()
        return all_info

DBManager().refresh_tables()
