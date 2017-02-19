import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

from alfred import alfred_globals as ag

Base = declarative_base()


class ModuleInfo(Base):
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


SessionMaker = None


def init_db():
    filepath = os.path.join(ag.user_folder_path, ag.db_name)
    engine = create_engine('sqlite:///{}'.format(filepath))
    Base.metadata.bind = engine
    if not os.path.isfile(filepath):
        Base.metadata.create_all()
    global SessionMaker
    SessionMaker = sessionmaker(engine)


def make_session():
    if SessionMaker is None:
        init_db()
    return SessionMaker()


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