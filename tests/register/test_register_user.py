from fixtures.api_client import ClientApi
from fixtures.register.models.register import RegisterModel


class TestRegister:
    def test_register_random_data(self, app: ClientApi):
        """
        1. Try to register new user
        2. Check response
        3. Check status code is 201
        """
        data = RegisterModel.random()
        res = app.register.register(data=data)
        assert res.status_code == 201
        assert res.body.uuid
        assert res.body.description == "User created successfully."
