from Sensor.exception import SensorException
import os,sys

from Sensor.logger import logging
from Sensor.utils import dump_csv_file_mongodb_collection

# def test_exception():
#     try:
#         logging.info("intentionally causing error to check if it's working")
#         b = 1/0
#
#     except Exception as e:
#         raise SensorException(e,sys)


# if __name__ == "__main__":
#     try:
#         test_exception()
#     except Exception as e:
#         print(e)
#
#


if __name__ == "__main__":
    file_path =r"C:\prabhakar\projects\live-sensor-fault-detection\aps_failure_training_set1.csv"
    database_name = "machinelearningdb"
    collection_name = "sensormlcollection"
    dump_csv_file_mongodb_collection(file_path,database_name,collection_name)
