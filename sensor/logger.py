import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime().now().strftime('%m%d%Y_%H%M%S')}.log"

LOG_FILE_DIR = os.path.join(os.getcwd(),"logs)")



LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)