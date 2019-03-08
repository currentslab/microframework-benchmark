from locust import HttpLocust, TaskSet, task
HOST = '172.105.226.70'
PORT = 8000

class TextTasks(TaskSet):
    
    @task
    def index(self):
        self.client.get("/text")

class TextUser(HttpLocust):
    host = "http://{}:{}".format(HOST, PORT)
    task_set = TextTasks
    min_wait = 5000
    max_wait = 15000
