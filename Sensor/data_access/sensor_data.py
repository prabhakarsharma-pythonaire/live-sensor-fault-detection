import sys
from typing import Optional

import numpy as np
import pandas as pd
import json

from numpy.core.records import record
from Sensor.configuration.mongo_db_connection import MongoDBClient
from Sensor.constant.database import DATABASE_NAME
from Sensor.exception import SensorException


class SensorData:
    """
    This class helps to export entire MongoDB records as pandas DataFrame.
    """

    def __init__(self):
        try:
            # Initialize MongoDB client
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise SensorException(e, sys)

    def save_csv_file(self, file_path: str, collection_name: str, database_name: Optional[str] = None) -> int:
        """
        Save the CSV file to MongoDB collection.
        - file_path: Path to the CSV file.
        - collection_name: The MongoDB collection where data will be inserted.
        - database_name: Optional name of the database to use (if None, the default database is used).

        Returns: The number of records inserted into MongoDB.
        """
        try:
            # Read CSV data into pandas dataframe
            data_frame = pd.read_csv(file_path)
            data_frame.reset_index(drop=True, inplace=True)

            # Convert dataframe to MongoDB-compatible format
            records = list(json.loads(data_frame.T.to_json()).values())

            # Get the MongoDB collection to insert data into
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            # Insert records into the MongoDB collection
            collection.insert_many(records)

            return len(records)
        except Exception as e:
            raise SensorException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Export MongoDB collection as a pandas DataFrame.
        - collection_name: Name of the collection to export.
        - database_name: Optional name of the database (if None, default database is used).

        Returns: A pandas DataFrame representing the MongoDB collection.
        """
        try:
            # Get the MongoDB collection to export data from
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            # Fetch data from MongoDB and convert to pandas DataFrame
            df = pd.DataFrame(list(collection.find()))

            # Drop the '_id' column if it exists
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            # Replace "na" with NaN values
            df.replace({"na": np.nan}, inplace=True)

            return df
        except Exception as e:
            raise SensorException(e, sys)
