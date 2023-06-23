from fixtures.api_client import ClientApi
from fixtures.auth.models.auth import AuthModel


class TestAuth:
    def test_auth_random_data(self, app: ClientApi):
        """
        1. Try to auth user with random data
        2. Check response
        3. Check status code is 401
        """
        data = AuthModel.random()
        res = app.auth.login(data=data)
        assert res.status_code == 401
        assert res.error_body.status_code == 401
        assert res.error_body.description == "Invalid credentials"
        assert res.error_body.error == "Bad Request"
