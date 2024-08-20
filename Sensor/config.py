from dataclasses import dataclass
import os
import pymongo



@dataclass

class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVariable()

# env_var = MongoDBConfig()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)

# mongo_db = mongo_client[env_var.mongo_db_name]
#
# mongo_collection = mongo_db[env_var.collection_name]