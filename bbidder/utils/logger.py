from bbidder.utils.config import Config
import logging
import datetime
import os

class Logger(logging.Logger):
    map_level = {
        'info':logging.INFO,
        'debug':logging.DEBUG,
        'warning':logging.WARN,
        'error': logging.ERROR
        }
    def setLogLevel(self, level):
        logging.Logger.setLevel(self, self.map_level[level])

log_level = Config.getParam('log', 'level')
log_file = Config.getParam('log', 'file')
log_file_path = os.path.join(os.path.abspath(os.getcwd()), log_file)
logger = Logger(__name__)
logger.setLogLevel(log_level)
sh = logging.StreamHandler()
logger.addHandler(sh)
logger.addHandler(logging.FileHandler(log_file_path))
        