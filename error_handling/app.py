from flask import *
from flask_cors import *

from error_advice import *

app = Flask(__name__)
app.register_blueprint(advice)


@app.route('/', methods=['GET'])
def index():
    return "home"


@app.route('/<err>', methods=['GET'])
def error(err):
    if err == "RuntimeError":
        raise RuntimeError("Learn SQL")
    if err == "TypeError":
        raise TypeError("Read Textbooks")
    if err == "ValueError":
        raise ValueError("Do Research")
    return "success"


if __name__ == '__main__':
    CORS(app)  # lets other programs consume app
    app.debug = True
    app.run()
