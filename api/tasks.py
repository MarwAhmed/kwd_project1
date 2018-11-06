from flask_restful import Resource
from flask import request
from db_query import DbConnection
import json
import array
import re


#def check_if_none(pattern, string_):
 #   return re.match(pattern, string_)

class TasksApi(Resource):

   # def get(self,parameter):
    #    return {'hello': parameter}


    def get(self, info_string):
         # 1d.all  Id.open_tasks  Id.
         data=''
         match_user = r"user='(\w+)"
         match_status = r"status='(\w+)"

         user_name = re.findall(match_user, info_string)
         user_status = re.findall(match_status, info_string)

         print(user_name[0])
         print(user_status[0])

         if (user_name[0] == '0') and (user_status[0] != '0'):
             data = DbConnection.get_of_staus(user_status[0])

         if (user_name[0] != '0') and (user_status[0] == '0'):
             data = DbConnection.get_of_creation_editor(user_name[0])

         if (user_name[0] != '0') and (user_status[0] != '0'):
             data = DbConnection.get_the_tasks_for_the_user(user_name[0], user_status[0])

         if (user_name[0] == '0') and (user_status[0] == '0'):
             data = DbConnection.get_tasklist()

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



