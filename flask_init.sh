RED='\u001b[31m'
GREEN='\u001b[32m'
BLUE='\u001b[34m'
YELLOW='\u001b[33m'

# usage
DIR=$1
echo "creating flask project..."
if [ -z $DIR ]; then
    echo -e ${RED}"Usage: $ ./flask_init <ROJECT_NAME>"
    exit
fi

mkdir $DIR

# main app
echo "
from flask import *
from flask_cors import *
from util.error_advice import advice

app = Flask(__name__)
app.register_blueprint(advice)

@app.route('/', methods=['GET'])
def index():
    return 'hello world'

if __name__ == '__main__':
    CORS(app) # lets other programs consume app
    app.debug = True
    app.run()
" >> $DIR"/app.py"

# create .gitignore
echo -e "${BLUE}Creating $DIR/.gitignore"
echo ".idea/
*/__pycache__
.vscode
*/sandbox.*
*/*.log
*/**/__pycache*
*/*.diff" >> $DIR"/.gitignore"

# create install requirements
echo -e "${BLUE}Creating $DIR/requirements.txt"
echo "dnspython==2.0.0
Flask==1.1.2
Flask-Cors==3.0.9
gunicorn==20.0.4
pymongo==3.11.0" >> $DIR"/requirements.txt"

# create subdirectories
SUB_DIR=("api" "repository" "service" "test" "util")
for E in ${SUB_DIR[*]}; do
    echo -e "${BLUE}Creating $DIR"/"$E"
    mkdir $DIR"/"$E
done

# database cradentials
echo -e "${BLUE}Creating $DIR/repository/database.py"
echo "
DATABASE = 'ENTER DB NAME HERE'
HOST = 'ENTER HOST HERE'
PORT = 'ENTER PORT HERE' # enter as an int value
URI = 'ENTER DB URI HERE'
" >> $DIR"/repository/database.py"

# create unit tests
echo -e "${BLUE}Creating $DIR/test/tests.py"
echo "
import unittest


# TODO: write unit tests
class MyTestCase(unittest.TestCase):
    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
">>$DIR"/test/tests.py"

# create error logging file
echo "import logging

logging.basicConfig(level=logging.DEBUG, filename='err.log')
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())


def log(exception):
    ex_name = type(exception).__name__
    message = f'{ex_name}: {exception}'
    logger.debug(message)
" >>$DIR"/util/logger.py"


echo "from flask import Blueprint
from util.logger import log

advice = Blueprint('advice', __name__)


# error advice
@advice.app_errorhandler(Exception)
def handle_general_error(e: Exception):
    log(e)
    message = str(e)
    return {f'{type(e).__name__}': message}, 400
" >>$DIR"/util/error_advice.py"

# getting started
echo -e "${YELLOW}Prerequisites:
$ cd $DIR
$ pip install -r requirements.txt"
echo -e "${GREEN}DONE! Happy devloping :)"