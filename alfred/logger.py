import sys

from logbook import Logger as l, StreamHandler

import alfred.alfred_globals as ag
from alfred.utils import Singleton
from alfred.utils.helpers import global_file_path


class Logger(metaclass=Singleton):
    def __init__(self):
        self._logger = l(ag.APP_NAME)
        log_file = open(global_file_path(ag.LOG_FILE), 'w')
        StreamHandler(log_file).push_application()
        StreamHandler(sys.stdout, bubble=True).push_application()

    def info(self, msg):
        self._logger.info(msg)

    def err(self, msg):
        self._logger.error(msg)
