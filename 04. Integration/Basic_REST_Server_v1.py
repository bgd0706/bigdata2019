from flask import Flask
from flask_restful import Resource, Api
# py -m pip install flask_restful <- 반드시 해당 커맨드로 인스톨 할 것
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource) :
    def get(self):
        return { 'hello' : 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__' :
    app.run(host='218.51.230.213')