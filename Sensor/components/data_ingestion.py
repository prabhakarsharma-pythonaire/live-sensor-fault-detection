

from Sensor.exception import SensorException
from Sensor.logger import logging
import os,sys
from pandas import DataFrame
from Sensor.entity.config_entity import DataIngestionConfig
from Sensor.entity.artifact_entity import DataIngestionArtifact
from Sensor.data_access.sensor_data import SensorData
from sklearn.model_selection import train_test_split


class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'>>' * 20}Data Ingestion log started.{'<<' * 20} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)


    def export_data_into_feature_store(self)-> DataFrame:
        """Export Mongo db collection records as data frame"""
        try:
            logging.info("Exporting data into feature store")

            sensor_data = SensorData()

            dataframe = sensor_data.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name
            )

            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)

            dataframe.to_csv(feature_store_file_path,index=False,header=True)

            return dataframe
        except Exception as e:
            raise SensorException(e, sys)


    def split_data_as_train_test(self,dataframe:DataFrame)-> None:
        try:
            train_set,test_set = train_test_split(
                dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)

            logging.info("Performed train test split")

            logging.info("Exited split_data_as_train_test method of data ingestion class")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)

            os.makedirs(dir_path,exist_ok=True)

            logging.info(f"Exporting train and test file path.")

            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)

            test_set.to_csv(
                self.data_ingestion_config.test_file_path,index=False,header=True
            )

            logging.info("Exported train and test file path.")

        except Exception as e:
            raise SensorException(e, sys)