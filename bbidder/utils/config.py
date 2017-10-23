import configparser
import datetime
import os
import json 
import simplejson

def getConfig(file):
        config = configparser.ConfigParser()
        config.read(file)
        if len(config.sections()) == 0:
            raise Exception('Could not parse configuration file. Aborting.')     
        return config
    
class Config:
    CONFIG_FILE = "../bidder.conf"
    config = getConfig(os.path.join(os.path.abspath(os.path.dirname(__file__)), CONFIG_FILE))
    
    @classmethod
    def getParam(cls, section, attr):
        return cls.config[section][attr]
    
    @classmethod
    def getMockedCampaigns(cls):
        mock = cls.getParam('campaignresponse', 'mock')
        params_file = cls.getParam('campaignresponse', 'mockjsonfile')
        params_filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../"+params_file)
        if mock:
            paramsfile = open(params_filepath, 'r')
            # Read the file's data
            try:
                data = json.load(paramsfile)
            except simplejson.scanner.JSONDecodeError:
                logger.error('Did not get valid json response:{0}. Giving up.'.format(data))
            except Exception as error:               
                logger.error('Error encountered in loading paramsfile to json: {0}'.format(error))  
            return data    
        else:
            return None
    