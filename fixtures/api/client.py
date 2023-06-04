from requests import Response
import requests


class Client:
    def request(self, method: str, url: str, **kwargs) -> Response:
        return requests.request(method, url, **kwargs)
