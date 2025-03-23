import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.log"

# Create logs directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Define log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] : %(lineno)d : %(levelname)s : %(message)s",
)
