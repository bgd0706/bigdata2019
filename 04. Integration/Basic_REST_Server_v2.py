from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.debug = True
api = Api(app)

class CreateUser(Resource) :
    def get(self):
        return {'status' : 'success'}
api.add_resource(CreateUser, '/user')

class CreateUser2(Resource) :
    def get(self):
        return {'status' : 'success'}
api.add_resource(CreateUser2, '/user2')

class Multi (Resource) :
    def get(self, num):
        return {'return':num*10}

api.add_resource(Multi, '/multi/<int:num>')
if __name__ == '__main__' :
    app.run(host='218.51.230.213')