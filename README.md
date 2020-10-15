<img src="img/flask-logo.png" width="200">

## Prerequisites

### Software
- <a href="https://www.postman.com/downloads/">Postman</a>
- <a href = "https://www.python.org/downloads/">Python 3</a>
- <a href = "https://www.jetbrains.com/pycharm/download/">Pycharm</a>
- <a href = "https://www.mongodb.com/try/download/enterprise">MongoDB</a>

### Set up MongoDB

https://github.com/alanngo/MongoDB

### Install Python Packages

#### Command Line
```bash

$ sudo pip3 install -r requirements.txt
```

#### Pycharm
1. Tools => Sync Python Requirements
2. Make sure your settings match image below

<img src= "img/requirements.PNG">


## Starter Code
```python
from flask import *
from flask_cors import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "hello world"

if __name__ == '__main__':
    CORS(app) # lets other programs consume app
    app.debug = True
    app.run()

```
## Important Concepts
### Basics
```python
# foo will execute if a GET or POST request is made with 'pancakes' in the URL
# 1st argument: route name. 2nd argument: API requests 
@app.route('/pancakes', methods=['GET', 'POST']) 
def foo(): # EX: http://localhost:5000/pancakes
    return "pancake jokes are so flat"
# functions decorated w/ @app.route CAN ONLY return the following...
# - string (HTML)
# - dictionary (JSON)
# - tuple
# - Response instance
# - WSGI callable
```

### Path Variable
```python
# to inject a path variable, use '<>'
# argument name in foo must match argument name in app.route
# in foo, 'key' is our path variable that we substitute in the URL
@app.route('/computers/<key>', methods=['GET'])
def foo(key):  # EX: http://localhost:5000/computers/windows
    table = \
        {
            "chromebook": "terrible",
            "mac": "good but too expensive",
            "pc": "amazing"
        }
    return {key: table[key]}

# you can also inject multiple path variables
# make sure the names in '<>' in app.route match the functions argument ver batim
@app.route('/company/<arg0>/<arg1>', methods=['GET'])
def bar(arg0, arg1):  # EX: http://localhost:5000/company/shantanu/infosys
    return f"Hello My name is {arg0}, I work at {arg1}"
```


### Query Parameter
```python
# leave the route alone
@app.route('/ut', methods=['GET'])
def data(): # EX: http://localhost:5000/ut?subject=research
    fav_subject = request.args.['subject'] # this line of code is important
    return f"6627 56837 {fav_subject}"
```

### Loading JSON request body
```python
@app.route('/', methods=['GET'])
def foo():
    # THIS SNIPPET IS REQUIRED TO LOAD JSON DATA
    obj = request.get_json() 
    return obj
```

### Error Handling
```python
@app.errorhandler(Exception) # this advice handles all errors
def handle_general_error(e: Exception):
    message = str(e)
    return {"Error": f"{message}"}, 400

@app.errorhandler(RuntimeError) # this advice handles all instances of runtime errors
def handle_runtime_error(e: RuntimeError):
    message = str(e)
    return {"RuntimeError": f"{message}"}, 404

@app.errorhandler(ValueError) # this advice handles all instances of value errors
def handle_value_error(e: ValueError):
    message = str(e)
    return {"ValueError": f"{message}"}, 403
```
## Deployment

### Heroku
https://github.com/alanngo/heroku-flask
