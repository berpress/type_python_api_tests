import json
import logging
from typing import TypeVar, Type

from requests import Response

from fixtures.api.models.client import CustomRequests, CustomResponse, ErrorBody

logger = logging.getLogger("api")

T = TypeVar("T")


def structure(response: Response, type_response: Type[T]) -> CustomResponse[T]:
    url = response.url
    assert isinstance(response.request.method, str)
    method = response.request.method
    status_code = response.status_code
    request_time = response.elapsed.total_seconds()
    headers = dict(response.request.headers)
    request: CustomRequests = CustomRequests(
        body=_get_body_request(response), method=method, url=url
    )
    if status_code >= 400:
        body_error = ErrorBody(**response.json())
    else:
        body_error = ErrorBody()
    if 200 <= status_code < 400:
        body = type_response(**response.json())
    else:
        body = None
    custom_response: CustomResponse = CustomResponse(
        url=url,
        method=method,
        status_code=status_code,
        body=body,
        request=request,
        request_time=request_time,
        error_body=body_error,
        headers=headers,
    )
    return custom_response  # type: ignore


def _get_body_request(response: Response) -> str | dict:
    body = response.request.body
    if body is None:
        return {}
    elif isinstance(body, bytes):
        return json.loads(body.decode("utf-8"))
    elif isinstance(body, str):
        return body
    return {}
