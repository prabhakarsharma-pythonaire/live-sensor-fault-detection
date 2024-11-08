from dotenv import load_dotenv
import pymongo
from Sensor.constant.database import DATABASE_NAME
import certifi

ca = certifi.where()
from Sensor.constant.env_variable import MONGODB_URL_KEY
import os
import logging

load_dotenv()


class MongoDBClient:
    client = None

    def __init__(self,database_name = DATABASE_NAME)->None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                logging.info(f"Retrieved mongo db url: {mongo_db_url}")

                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile = ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]

        except Exception as e:
            logging.error(f"Error while connecting to mongoDB: {e}")
            raise

