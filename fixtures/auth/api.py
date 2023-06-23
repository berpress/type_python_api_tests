from common.deco.request_logger import log
from fixtures.api.models.client import CustomResponse
from fixtures.api.structure import structure
from fixtures.auth.models.auth import AuthResponse, AuthModel


class Auth:
    def __init__(self, app):
        self.app = app

    _POST_AUTH = "/auth"

    @log("Login new user")
    def login(self, data: AuthModel) -> CustomResponse[AuthResponse]:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/auth/authUser # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self._POST_AUTH}",
            json=data.dict(),
        )
        return structure(response=response, type_response=AuthResponse)
