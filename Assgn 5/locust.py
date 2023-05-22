from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    @task
    def index(self):
        self.client.get("/")
        self.client.get("/register/student")
        self.client.get("/register/teacher")
        self.client.get("/login/student")
        self.client.get("/login/teacher")
        self.client.get("/quiz/create")
        self.client.get("/quiz/view")
        self.client.get("/quiz/details")
        self.client.get("/quiz/attempt")
        self.client.get("/quiz/result")