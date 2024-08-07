import os
from yaml import safe_load
from .pattern_helper import singleton

class Configuration:
    def __init__(self) -> None:
        self.default_configs = {}
        configPath = 'api-service\configs\default_config.yml'
        path = os.getcwd()      
        self.config_file = os.path.join(path, configPath)
        
        with open(self.config_file) as file:
            self.default_configs = safe_load(file)

    def get(self, key):
        if os.getenv(key) is None:
            return self.default_configs['configs'][key]
        return os.getenv(key) 