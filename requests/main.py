from flask import jsonify, request, Flask
from Student import *
HOST = 'localhost'
PORT = 5000

app = Flask(__name__)
student_id = 2


# example reference code

# runs if a GET request is made
@app.route('/', methods=['GET'])
def get_req():
    return "using get request"


# runs if a POST request is made
@app.route('/', methods=['POST'])
def post_req():
    return "using post request"


# runs if a PUT request is made
@app.route('/', methods=['PUT'])
def put_req():
    return "using put request"


# runs if a DELETE request is made
@app.route('/', methods=['DELETE'])
def delete_req():
    return "using delete request"


students = \
    {
        Student(sid=0, name="omar", language="shell", framework="flask", loves="research"),
        Student(sid=1, name="angela", language="python", framework="react", loves="data science")
    }


@app.route('/students', methods=['GET'])
def get_students():
    json_list = []
    for s in students:
        json_list.append(s.__dict__)
    return jsonify(json_list)


@app.route('/students/<id>', methods=['GET'])
def get_student(id: int):
    err = 'error'
    msg = f"no student with id {id}"
    for s in students:
        tmp = Student(sid=id, name=None, language=None, framework=None, loves=None)
        if tmp.__eq__(s):
            return s.__dict__
    return {err: msg}


@app.route('/students', methods=['POST'])
def add_student():
    global student_id
    student_id = student_id + 1
    data = request.get_json()
    student = Student(
        sid=student_id,
        name=data['name'],
        language=data['language'],
        framework=data['framework'],
        loves=data['loves'])
    students.add(student)

    return student


@app.route('/students', methods=['PUT'])
def update_student():
    return "todo"


def main():
    app.debug = True
    app.run(HOST, PORT)


main()
