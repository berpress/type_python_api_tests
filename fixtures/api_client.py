from fixtures.api.client import Client
from fixtures.auth.api import Auth
from fixtures.register.api import Register


class ClientApi:
    def __init__(self, url: str):
        self.url = url
        self.client = Client()
        self.auth = Auth(self)
        self.register = Register(self)
