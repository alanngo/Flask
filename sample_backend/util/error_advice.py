from flask import Blueprint

from util.logger import log

advice = Blueprint("advice", __name__)


@advice.app_errorhandler(Exception)
def general_error_advice(e: Exception):
    log(e)
    message = str(e)
    return {f"{type(e).__name__}": message}, 400
