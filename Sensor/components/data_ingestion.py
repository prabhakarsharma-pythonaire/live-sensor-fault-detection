from multiprocessing.reduction import sendfds

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


    def export_data_into_feature_store(self)->DtatFrame:
        """Export Mongo db collection records as data frame"""
        try:
            logging.indo("Exporting data into feature store")

            sensor_data = SensorData()

            dataframe = sensor_data.export_collection_as_dataframe(

            )