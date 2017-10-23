import configparser
import logging
import datetime
import os

def getConfig(file):
        config = configparser.ConfigParser()
        config.read(file)
        if len(config.sections()) == 0:
            raise Exception('Could not parse configuration file. Aborting.')     
        return config
    
class Config:
    CONFIG_FILE = "bidder.conf"
    config = getConfig(CONFIG_FILE)
    
    @classmethod
    def getParam(cls, section, attr):
        return cls.config[section][attr]
'''
class Logger(logging.Logger):
        
    map_level = {
        'info':logging.INFO,
        'debug':logging.DEBUG,
        'warning':logging.WARN,
        'error': logging.ERROR
        }    
    
    def __init__(self, dir='logs', level='info', func='log'):
        now = datetime.datetime.now().strftime('%Y%m%d_%H:%M:%S')
        logfile = os.path.join(dir, '{0}_{1}.log'.format(func, now))
        logging.Logger.addHandler(self, logging.FileHandler(logfile))
        logging.Logger.addHandler(self, logging.StreamHandler())
        logging.Logger.addHandler(self, logging.FileHandler(logfile))
        logging.Logger.setLevel(self, self.map_level(level))
    
    def setLogLevel(self, level):
        self.setLevel(self.map_level(level))
'''
class Logger(logging.Logger):
    pass

logger = Logger(__name__)
logger.setLevel(logging.INFO)
sh = logging.StreamHandler()
logger.addHandler(sh)
        