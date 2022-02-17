
from crypt import methods

from flask import Flask, request
from flask import jsonify

GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'
PUT = 'PUT'

OK = 200
FORBIDDEN = 403


app = Flask(__name__)


@app.route('/')
def default():
    return 'Some text'

@app.route('/dvl', methods=(GET, ))
def get_dvl_info():
    if request.method == GET:
        return 'Dummy DVL DATA', OK
    else:
        return 'Only GET requests', FORBIDDEN






