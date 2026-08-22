import os
import pandas as pd
import sys
from src.ML_PROJECT import logger
from src.ML_PROJECT.exception import customeException
from dataclasses import dataclass
from src.ML_PROJECT.utils import read_sql_data
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join("artifacts","train.csv")
    test_data_path : str=os.path.join("artifacts","test.csv")
    row_data_path : str=os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion=DataIngestionConfig

    def read_data(self):
        try:
            logger.logging.info("Start Reading Data From Sql")
            df = read_sql_data()
            logger.logging.info("complete Reading Data From Sql")
            os.makedirs(os.path.dirname(self.data_ingestion.row_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion.row_data_path,index=False, header=True)
            logger.logging.info("Raw.csv file create successfully")

            train_dataset, test_dataset=train_test_split(df, test_size=0.20, random_state=42)

            train_dataset.to_csv(self.data_ingestion.train_data_path, index=False, header=True)
            logger.logging.info("train.csv file created successfully")

            test_dataset.to_csv(self.data_ingestion.test_data_path, index=False, header=True)
            logger.logging.info("test.csv file created successfully")

            return(
                self.data_ingestion.train_data_path,
                self.data_ingestion.test_data_path,
            )
        except Exception as e:
            raise customeException(e, sys)

