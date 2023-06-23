from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class ErrorBody(BaseModel):
    description: str | None = None
    error: str | None = None
    status_code: int | None = None


class CustomRequests(BaseModel, Generic[T]):
    body: T | None
    method: str | None
    url: str


class CustomResponse(BaseModel, Generic[T]):
    url: str
    method: str
    status_code: int
    request_time: float = -1
    body: T | None
    headers: dict = {}
    request: CustomRequests | None
    error_body: ErrorBody
