import psycopg2
import datetime

class DbConnection:
    DB_PARAMS = {
        'database': 'kwd_tasks',
        'user': 'kwd_user',
        'password': 'password',
        'host': '127.0.0.1',
        'port': '5432'
    }

    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()



    @classmethod
    def get_tasklist(cls):
        cls.cur.execute("SELECT * from tasks")

        results = cls.cur.fetchall()

        data = list()

        for row in results:

            data.append(
                {
                    'task_url': row[0],
                    'task_id': row[1],
                    'task_editor': row[2],
                    'task_staus': row[3],
                    #'task_created_on': row[4],

                }
            )

        return data



    @classmethod
    def get_tasks_status(cls,status_value):
        sql= "SELECT * from tasks WHERE task_status = %"
        val = (status_value,)
        cls.cur.execute(sql, val)

        results = cls.cur.fetchall()

        data = list()

        for row in results:
            data.append(
                {
                    'task_url': row[0],
                    'task_id': row[1],
                    'task_editor': row[2],
                    'task_staus': row[3],
                }
            )

        return data





    @classmethod
    def write_task(self, task_url, task_editor, task_status):
        sql = "INSERT INTO tasks (task_url, task_editor, task_status ,task_created_on,task_updated_on) VALUES (%s, %s , %s ,%s,%s)"
        now = datetime.datetime.now()
        val = (task_url,task_editor,task_status,now,now)
        self.cur.execute(sql,val)
        self.conn.commit()




    @classmethod
    def get_of_creation_editor(cls , editor_value):

        sql="SELECT * FROM tasks WHERE task_editor = %s"
        val=(editor_value,)
        cls.cur.execute(sql,val)
        results = cls.cur.fetchall()

        data = list()

        for row in results:
            data.append(
                {
                    'task_url': row[0],
                    'task_id': row[1],
                    'task_editor': row[2],
                    'task_staus': row[3],

                }
            )

        return data



    @classmethod
    def update_status(cls,task_id_value,task_status_value):
        sql = "UPDATE tasks SET task_status = %s ,task_updated_on = %s WHERE task_id = %s "
        now = datetime.datetime.now()
        val = (task_status_value, now , task_id_value)
        cls.cur.execute(sql,val)
        cls.conn.commit()



    #def get_of_editor(cls):

