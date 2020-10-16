from datetime import *
import logging

logging.basicConfig(level=logging.DEBUG, filename="err.log")
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
now = datetime.now()


def __write(message):
    f = open(f"err.log", 'a')
    f.write(message)
    f.close()


def log(exception):
    ex_name = type(exception).__name__
    message = f"{ex_name}: {exception}"
    logger.debug(message)
