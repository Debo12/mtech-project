from pymongo import MongoClient
from helpers.pattern_helper import singleton
import logging
from helpers.initializer import Configuration

config = Configuration()

class BaseDAO:    
    def __init__(self):
        self.client = MongoClient(config.get('MONGODB_URI'))

    def get_db_connection(self):
        db = self.client.get_database()
        return db
