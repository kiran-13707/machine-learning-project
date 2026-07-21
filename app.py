from src.ML_PROJECT import logger
from src.ML_PROJECT.exception import customeException
import sys

try:
    a=10
    b=0
    c=a / b
except Exception as e:
    logger.logging.info(customeException(e, sys))
    raise Exception(e, sys)