from flask import *

from MongoDB import MongoDB

# runtime configurations
HOST = 'localhost'
PORT = 5000
MONGO_PORT = 27017
# cluster = MongoClient('localhost', 27017)
# db = cluster['college']
# collection = db['student']
m = MongoDB(host=HOST, port=MONGO_PORT, database="college", doc="student")

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_students():
    return m.find_all()


@app.route('/<id>', methods=['GET'])
def get_student_by_id(id):
    return m.find_by_id(id)


def main():
    app.debug = True
    app.run(HOST, PORT)


main()
