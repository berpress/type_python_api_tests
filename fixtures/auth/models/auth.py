from faker import Faker
from pydantic import BaseModel

fake = Faker()


class AuthModel(BaseModel):
    username: str | None
    password: str | None

    @staticmethod
    def random():
        return AuthModel(username=fake.email(), password=fake.password())


class AuthResponse(BaseModel):
    access_token: str
