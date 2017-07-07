import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

from alfred import alfred_globals as ag
from alfred.utils import Singleton


class DBManager(metaclass=Singleton):
    DBModelBase = declarative_base()

    def __init__(self):
        filepath = os.path.join(ag.user_folder_path, ag.db_name)
        self.engine = create_engine('sqlite:///{}'.format(filepath))
        self.DBModelBase.metadata.bind = self.engine
        self.refresh_tables()

    def session(self):
        return sessionmaker(self.engine)()

    def refresh_tables(self):
        self.DBModelBase.metadata.create_all()
