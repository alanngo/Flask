from flask import jsonify, request, Flask
from Student import Student

HOST = 'localhost'
PORT = 5000

app = Flask(__name__)


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
    [
        Student(name="omar", language="shell", framework="flask", loves="research"),
        Student(name="angela", language="python", framework="react", loves="data science")
    ]


@app.route('/students', methods=['GET'])
def get_students():
    json_list = []
    for s in students:
        json_list.append(s.__dict__)
    return jsonify(json_list)


@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    students.append(Student(
        name=data['name'],
        language=data['language'],
        framework=data['framework'],
        loves=data['loves']
        ))
    return data


def main():
    app.debug = True
    app.run(HOST, PORT)


main()
