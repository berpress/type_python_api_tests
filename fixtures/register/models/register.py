from faker import Faker
from pydantic import BaseModel

fake = Faker()


class RegisterModel(BaseModel):
    username: str | None
    password: str | None

    @staticmethod
    def random():
        return RegisterModel(username=fake.email(), password=fake.password())


class RegisterUserResponse(BaseModel):
    description: str
    uuid: int
