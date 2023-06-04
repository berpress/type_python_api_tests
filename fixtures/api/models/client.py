from enum import Enum
from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class MethodType(str, Enum):
    POST = "POST"
    PUT = "PUT"
    GET = "GET"
    DELETE = "DELETE"


class ErrorBody(BaseModel):
    description: str | None = None
    error: str | None = None
    status_code: int | None = None


class CustomRequests(BaseModel, Generic[T]):
    body: T | None
    headers: dict
    method: str | None
    url: str


class CustomResponse(BaseModel, Generic[T]):
    url: str
    method: str | None
    status_code: int
    request_time: float = -1
    body: T
    headers: dict = {}
    request: CustomRequests | None
    error_body: ErrorBody
