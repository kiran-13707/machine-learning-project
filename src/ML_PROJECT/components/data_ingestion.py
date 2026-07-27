import os
import pandas as pd
from src.ML_PROJECT.exception import customeException
from src.ML_PROJECT.logger import logging
from dataclasses import dataclass

@dataclass
class DataIngetionConfig:
    train_data_path : str=os.path.join("Artifacts","train.csv")
    test_data_path : str=os.path.join("Artifacts","test.csv")
    raw_data_path : str=os.path.join("Artifacts","raw.csv")

class DataIngetion:
    def __init__(self):
        self.ingetionconfig=DataIngetionConfig()