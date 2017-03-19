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

    def __init__(self, name, source, user, version):
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
    def all(cls):
        return DBManager().session.query(ModuleInfo).all()
