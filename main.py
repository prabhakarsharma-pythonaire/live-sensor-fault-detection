from Sensor.exception import SensorException
import os,sys

from Sensor.logger import logging



def test_exception():
    try:
        logging.info("intentionally causing error to check if it's working")
        b = 1/0

    except Exception as e:
        raise SensorException(e,sys)


if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)


https://github.com/avnyadav/sensor-fault-detection/blob/main/aps_failure_training_set1.csv