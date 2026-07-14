from datetime import datetime
import os
import logging

LOG_FILE=f"{datetime.now().strftime("%m_%d_%Y, %H_%M_%S")}.log"
# print(LOG_FILE)
LOG_dir=os.path.join(os.getcwd(),"logs")
os.makedirs(LOG_dir, exist_ok=True)
LOG_PATH=os.path.join(LOG_dir, LOG_FILE)
# print(LOG_PATH)

logging.basicConfig(
    filename=LOG_PATH,
    format="[%(asctime)s] %(levelname)-8s | %(name)s | Line:%(lineno)d | %(funcName)s() | %(message)s",
    level=logging.INFO,
)

