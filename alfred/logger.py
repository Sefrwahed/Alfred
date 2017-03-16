from logbook import Logger as l, StreamHandler
import sys

# Local includes
from alfred.utils import Singleton
import alfred.alfred_globals as ag


class Logger(metaclass=Singleton):
    def __init__(self):
        self._logger = l(ag.APP_NAME)
        StreamHandler(sys.stdout).push_application()

    def info(self, msg):
        self._logger.info(msg)

    def err(self, msg):
        self._logger.error(msg)
