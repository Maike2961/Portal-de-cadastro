from locust import HttpUser, task, between

#teste de requisições
class HelloUser(HttpUser):
    wait_time = between(1, 2)
    
    @task
    def hello_world(self):
        data = {"nome": "teste", "email": "teste@teste.com.br", "senha": "123456"}
        self.client.post("/usuario", data=data)
        self.client.get("/")