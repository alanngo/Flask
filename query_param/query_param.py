from flask import *
from flask_cors import CORS

HOST = 'localhost'
PORT = 5000
app = Flask(__name__)


@app.route('/ut')
def data():
    fav_subject = request.args['subject']
    return f"6627 56837 {fav_subject}"


def main():
    CORS(app)
    app.debug = True
    app.run(HOST, PORT)


main()
