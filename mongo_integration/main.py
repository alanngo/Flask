from flask import *
from flask_cors import *
from MongoDB import MongoDB

# runtime configurations
HOST = 'localhost'
PORT = 5000
m = MongoDB(
    url="localhost:27017",
    database="college",
    doc="student"
)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_students():
    val = jsonify(m.find_all())
    return val


@app.route('/<id>', methods=['GET'])
def get_student_by_id(id):
    val = m.find_by_id(id)
    return val


@app.route('/', methods=['POST'])
def add_student():
    student = request.get_json()
    m.add(student)
    return student


@app.route('/<id>/<key>', methods=['PUT'])
def update_info(id, key):
    value = {"favorite db": "sql"}
    m.update_entry(id, key, value)
    return m.find_by_id(id)


@app.route('/<id>', methods=['DELETE'])
def remove_student(id):
    m.remove_by_id(id)
    return {"success": True}


def main():
    CORS(app)
    app.debug = True
    app.run(HOST, PORT)


main()
