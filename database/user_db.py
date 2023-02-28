"""
    Possible common methods can be used in the other controllers.
"""

from aws_lambda_powertools import Logger
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from settings import MONGO_URI, MONGO_DBNAME

class MongoDbUser():

    logging = Logger()

    try:
        mongo_db = MongoClient(
        MONGO_URI,
        maxPoolSize=50,
        maxIdleTimeMS=1000,
        waitQueueTimeoutMS=100)[MONGO_DBNAME]
    except Exception as ex:
        logging.info(f"Error during mongo connection {ex}")
        mongo_db = None


    @classmethod
    def get_user_id(cls,user):
        try:
            #id_user = user.get('_id')
            response_user = cls.mongo_db.user.find_one({'_id': ObjectId(user)})
            return response_user
        except Exception as ex:
            cls.logging.error(f'Error during get user {ex}')
            return False


    @classmethod
    def get_user_email(cls,user):
        try:
            email_user = user.get('email')
            response_user = cls.mongo_db.user.find_one({'email': email_user})
            return response_user
        except Exception as ex:
            cls.logging.error(f'Error during get user {ex}')
            return False


    @classmethod
    def insert_user(cls,user_email, user_pwd):
        try:
            response_user = cls.mongo_db.user.insert_one({
                'email': user_email,
                'password': user_pwd,
                'created': datetime.utcnow()})
            return response_user.inserted_id
        except Exception as ex:
            cls.logging.error(f'Error during insert user {ex}')
            return False
