'''
Created on Feb 25, 2015

@author: James Culbertson
'''
from ConfigParser import ConfigParser
import constants as c
import os.path

class Config(object):
    '''
    Loads and saves the configurations files.
    User config is read and written on demand.
    '''

    def __init__(self):
        self.user_config = {}
        self.load_user_config()
        
    def save_user_config(self):
        cfg_file = open(c.CONFIG_USER + ".ini","w")
        config = ConfigParser()
        config.add_section(c.CONFIG_USER)
        config.set(c.CONFIG_USER, c.CONFIG_USER_LAST_TEMPLATE_FILE, self.user_config[c.CONFIG_USER_LAST_TEMPLATE_FILE])
        config.write(cfg_file)
        cfg_file.close()
        
    def load_user_config(self):
        if os.path.exists(c.CONFIG_USER + ".ini"):
            config = ConfigParser()
            config.read(c.CONFIG_USER + ".ini")
            if config.has_section(c.CONFIG_USER):
                self.user_config[c.CONFIG_USER_LAST_TEMPLATE_FILE] = config.get(c.CONFIG_USER, c.CONFIG_USER_LAST_TEMPLATE_FILE).replace('"','')
                
        