import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

from alfred import alfred_globals as ag

DBModelBase = declarative_base()
SessionMaker = None


def init_db():
    filepath = os.path.join(ag.user_folder_path, ag.db_name)
    engine = create_engine('sqlite:///{}'.format(filepath))
    DBModelBase.metadata.bind = engine
    if not os.path.isfile(filepath):
        DBModelBase.metadata.create_all()
    global SessionMaker
    SessionMaker = sessionmaker(engine)


def make_session():
    if SessionMaker is None:
        init_db()
    return SessionMaker()
