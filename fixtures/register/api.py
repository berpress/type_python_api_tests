from common.deco.request_logger import log
from fixtures.api.models.client import CustomResponse
from fixtures.api.structure import structure
from fixtures.auth.models.auth import AuthModel
from fixtures.register.models.register import RegisterUserResponse


class Register:
    def __init__(self, app):
        self.app = app

    _POST_REGISTER = "/register"

    @log("Register new user")
    def register(self, data: AuthModel) -> CustomResponse[RegisterUserResponse]:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self._POST_REGISTER}",
            json=data.dict(),
        )
        return structure(response=response, type_response=RegisterUserResponse)
