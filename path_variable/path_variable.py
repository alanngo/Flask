from flask import *
from flask_cors import CORS

HOST = 'localhost'
PORT = 5000

app = Flask(__name__)


@app.route('/company/<arg0>/<arg1>', methods=['GET'])
def bar(arg0, arg1):  # EX: http://localhost:5000/company/shantanu/infosys
    return f"Hello My name is {arg0}, I work at {arg1}"


def main():
    CORS(app)
    app.debug = True
    app.run(HOST, PORT)


main()
