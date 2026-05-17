#default constructor
import os
import logging
from datetime import datetime
LOG_file_NAME=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR="logs"
LOG_FILE_PATH=os.path.join("logs",LOG_file_NAME)
os.makedirs(LOG_DIR,exist_ok=True)
logging.basicConfig(filename=LOG_FILE_PATH,
                    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
                    level=logging.DEBUG)
logging.info("Program logger.py started")
print("Print the start of the program")
