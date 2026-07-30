import os
import pandas as pd
import sys
from src.ML_PROJECT import logger
from src.ML_PROJECT.exception import customeException
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join("Artifacts","train.csv")
    test_data_path : str=os.path.join("Artifacts","test.csv")
    raw_data_path : str=os.path.join("Artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingetionconfig=DataIngestionConfig()

    def read_data(self):
        try:
            logger.logging.info("Start Reading Data From Sql")
            os.makedirs(os.path.dirname(self.data_ingestion.row_data_path),exist_ok=True)
            print("data path from another class", self.data_ingestion.test_data_path)

        except Exception as e:
            raise customeException(e, sys)

obj=DataIngestion()
obj.read_data()