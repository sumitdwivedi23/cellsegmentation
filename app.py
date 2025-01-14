from cellsegmentation.logger import logging
from cellsegmentation.exception import AppException
import sys

logging.info("Welcome to teh custom lgo")

try:
    a=4/"6"

except Exception as e:
    raise AppException(e, sys)
