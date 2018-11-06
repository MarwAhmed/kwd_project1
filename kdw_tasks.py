from api.tasks import Tasks
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
api.add_resource(Tasks, "/api/tasks/<info_string>")

if __name__ == '__main__':

    app.run(debug=True ,port=2523)