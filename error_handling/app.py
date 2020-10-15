from flask import *
from flask_cors import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "home"


@app.route('/<err>', methods=['GET'])
def error(err):
    if err == "RuntimeError":
        raise RuntimeError("Learn SQL")
    if err == "TypeError":
        raise RuntimeError("Read Textbooks")
    if err == "ValueError":
        raise ValueError("Do Research")
    return "success"


# error advice
@app.errorhandler(Exception)
def handle_general_error(e: Exception):
    message = str(e)
    return {"Error": f"6627 should {message}"}, 400


if __name__ == '__main__':
    CORS(app)  # lets other programs consume app
    app.debug = True
    app.run()
