from datetime import *
import logging

logging.basicConfig(level=logging.DEBUG, filename="err.log")
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())


def log(exception):
    ex_name = type(exception).__name__
    message = f"{ex_name}: {exception}"
    logger.debug(message)
