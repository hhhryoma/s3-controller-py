from asyncio.log import logger
from fileinput import close
from http import client
import logging
import pymongo
from bson.json_util import dumps

logger = logging.getLogger(__name__)

class MongoConnector():
    def __init__(self):
        pass
    def __enter__(self):
        pass
    def __exit__(self):
        pass


class MongoHandler():
    def __init__(self, db, client=None) -> None:
        if client == None:
            self.client = pymongo.MongoClient()
        else:
            self.client = client
        self.db = self.client[db]
        self.db_name = db 
        
    def __del__(self):
        self.client.close()
    
    def col(self):
        return self.db.list_collection_names()
    
    def watch(self, pipeline=[], options={}):
        return self.db.watch(pipeline, **options)


###################
# DB Config
###################

def enable_pre_and_post_image(col):
    pass

###################
# DB CRUD
###################
def find(client):
    return client.find()


def find_one(client):
    return client.find_one()


def insert_one(client, document):
    return client.insert_one(document)


def insert_many(client, document):
    return client.insert_many(document)


def delete_one(client, filter):
    return client.delete_one(filter)


def delete_many(client, filter):
    return client.delete_many(filter)


def wrap_str(list):
    s = ''
    for v in list:
        s += f'["{v}"]'
    return s

# client = pymongo.MongoClient()
# mongo = MongoHandler(client=client, db='test')

# col_test = mongo.db['test']
# print(mongo.col())


# print(client.admin.command({'setClusterParameter': { 'changeStreamOptions': { 'preAndPostImages': { 'expireAfterSeconds': "off" } } }}))
# print(client.admin.command( { 'getClusterParameter': "changeStreamOptions" } ))

# print(mongo.db.command({'setClusterParameter': { 'changeStreamOptions': { 'preAndPostImages': { 'expireAfterSeconds': "off" } } }}))
# print(mongo.db.command( { 'getClusterParameter': "changeStreamOptions" } ))

# mongo.db.command( {
#    'collMod': "test",
#    'changeStreamPreAndPostImages': { 'enabled': True }
# } )

# options = {
#     'full_document_before_change': 'whenAvailable', 
#     'full_document': 'updateLookup'
# }
# for event in mongo.watch(options=options):
#     event_json = dumps(event)
#     print(event)
# data = {'name': 'test_test', 'idx': 100}
# ret = insert_one(col_test, data)
# ret = find_one(col_test)    
# ret = find(col_test)    
    
# exit()
    
