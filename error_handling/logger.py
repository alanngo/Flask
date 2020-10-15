from datetime import *

now = datetime.now()


def __write(message):
    f = open(f"err.log", 'a')
    f.write(message)
    f.close()


def log(exception):
    ex_name = type(exception).__name__
    message = f"{now}: {ex_name} {exception}\n"
    __write(message)
    print(message)
