import os
import sys
from src.ML_PROJECT import logger
from src.ML_PROJECT.exception import customeException
from dotenv import load_dotenv

load_dotenv()

HOST=os.getenv("host")
ROOT=os.getenv("root")
PASSWORD=os.getenv("password")
DB=os.getenv("db")

def read_sql_data():
    print("ENV DATA :- ",HOST, ROOT, PASSWORD, DB)

