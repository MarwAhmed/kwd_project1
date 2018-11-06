from api.tasks import TasksApi
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
api.add_resource(TasksApi, "/api/tasks/<info_string>")

if __name__ == '__main__':

    app.run(debug=True ,port=2523)