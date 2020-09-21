from flask import *

app = Flask(__name__)


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


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
