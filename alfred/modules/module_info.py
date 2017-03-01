import os
from sqlalchemy import Column, Integer, String

from alfred import alfred_globals as ag
from alfred.database import DBModelBase, make_session


class ModuleInfo(DBModelBase):
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
        path = os.path.join(ag.modules_folder_path,
                            self.source,
                            self.user,
                            self.name)
        # TODO get path from database
        path = os.path.join(
            '/home/n1amr/.pyenv/versions/3.6.0/envs/env_alfred/lib/python3.6/site-packages',
            self.name

        )
        return path

    def training_sentences_json_file_path(self):
        return os.path.join(self.root(),
                            "training_sentences.json")

    def entry_point(self):
        return self.name + ".py"

    def class_name(self):
        s = self.name
        s = "".join(w.title() for w in s.split("-"))
        s = "".join(w.title() for w in s.split("_"))
        return s


def get_module_by_id(id):
    session = make_session()
    info = session.query(ModuleInfo).get(int(id))
    session.close()
    return info


def add_module_info(name, source, user, version):
    module = ModuleInfo(name, source, user, version)
    session = make_session()
    session.add(module)
    session.commit()
    session.close()


def get_all_module_info():
    session = make_session()
    all_module_info = session.query(ModuleInfo).all()
    session.close()
    return all_module_info


def delete_module_info(id):
    session = make_session()
    session.query(ModuleInfo).filter(ModuleInfo.id == id).delete()
    session.commit()
    session.close()
