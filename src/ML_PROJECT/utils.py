import os
import sys
from src.ML_PROJECT import logger
from src.ML_PROJECT.exception import customeException
from dotenv import load_dotenv
import pymysql
import pandas as pd

load_dotenv()

HOST=os.getenv("host")
USER=os.getenv("user")
PASSWORD=os.getenv("password")
DB=os.getenv("db")

def read_sql_data():
    # print("ENV DATA :- ",HOST, ROOT, PASSWORD, DB)
    logger.logging.info("Start a reading Data From MYSQL")
    try:
        connection_sql=pymysql.connect(user=USER,host=HOST,password=PASSWORD,db=DB)
        print("connrction succssfully")
        print(connection_sql)
    except Exception as e:
        logger.logging.info(customeException(e, sys))
        raise customeException(e, sys)

