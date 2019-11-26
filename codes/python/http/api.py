# =============================================================================
# Author: falseuser
# Created Time: 2019-08-26 15:31:19
# Last modified: 2019-08-26 15:31:57
# Description: api.py
# =============================================================================
from flask import Flask
from flask_restful import Api, Resource
from flask_httpauth import HTTPTokenAuth


APP = Flask(__name__)
API = Api(APP)
AUTH = HTTPTokenAuth(scheme='AUTH')


@AUTH.verify_token
def verify_token(token):
    print(token)
    if token == "11111":
        return True
    else:
        return False


class TestAPI(Resource):

    @AUTH.login_required
    def get(self):
        return 1


API.add_resource(TestAPI, "/test/")
if __name__ == '__main__':
    APP.run(host="0.0.0.0")
