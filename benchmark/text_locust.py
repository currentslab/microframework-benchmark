from locust import HttpLocust, TaskSet, task
from microframeworks.settings import HOST, PORT

class TextTasks(TaskSet):
    
    @task
    def index(self):
        self.client.get("/text")

class TextUser(HttpLocust):
    host = "http://{}:{}".format(HOST, PORT)
    task_set = TextTasks
    min_wait = 5000
    max_wait = 15000
