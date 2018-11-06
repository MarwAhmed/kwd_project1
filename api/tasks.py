from flask_restful import Resource
from flask import request
from db_query import DbConnection
import json
import array

class Tasks(Resource):

   # def get(self,parameter):
    #    return {'hello': parameter}

    def get(self, info_string):
         # 1d.all  Id.open_tasks  Id.
         selection_key = info_string.split('.')[0]
         selection_value = info_string.split('.')[1]
         data = ' Send me please witch tasks you need to get it '
         if selection_value == 'all':
             data = DbConnection.get_tasklist()

         if (selection_value == 'open_tasks') or (selection_value == 'finished' ) or (selection_value == 'started'):
             data = DbConnection.get_tasks_status(selection_value)

         if (selection_value == 'MK') or (selection_value == 'MA'):
             data = DbConnection.get_of_creation_editor(selection_value)
        # _data = json.loads(data)
         return data




    def post(self, info_string):
         t_url = request.json[0]["task_url"]
         t_editor = request.json[0]["task_editor"]
         t_status = request.json[0]["task_status"]
         print(t_url, t_editor, t_status)
         DbConnection.write_task(t_url, t_editor, t_status)
         return 200


    def put(self, info_string):
        task_id_value = info_string
        task_status_value = request.json['task_status']
        print(task_status_value)
        DbConnection.update_status(task_id_value,task_status_value)
        return 200 # this function to update the status of a task in the database



