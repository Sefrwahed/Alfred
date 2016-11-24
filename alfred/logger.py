from logbook import Logger, StreamHandler
import sys

# Local includes
import alfred.alfred_globals as ag


StreamHandler(sys.stdout).push_application()
_logger = Logger(ag.APP_NAME)

def info(msg):
    _logger.info(msg)
