from alfred.lib import Singleton

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

from alfred import alfred_globals as ag
from alfred.lib import Singleton


class DBManager(metaclass=Singleton):
    DBModelBase = declarative_base()

    def __init__(self):
        filepath = os.path.join(ag.user_folder_path, ag.db_name)
        engine = create_engine('sqlite:///{}'.format(filepath))
        self.DBModelBase.metadata.bind = engine

        if not os.path.isfile(filepath):
            self.DBModelBase.metadata.create_all()
        self.session = sessionmaker(engine)()

    def __del__(self):
        self.session.close()
