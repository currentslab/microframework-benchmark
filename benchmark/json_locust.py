from locust import HttpLocust, TaskSet, task

HOST = '172.105.226.70'
PORT = 8000

class JsonTasks(TaskSet):
    
    @task
    def index(self):
        self.client.get("/json")

class JsonUser(HttpLocust):
    host = "http://{}:{}".format(HOST, PORT)
    task_set = JsonTasks
    min_wait = 5000
    max_wait = 15000