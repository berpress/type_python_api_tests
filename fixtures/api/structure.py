import json
import logging
from typing import List, Any
from typing import TypeVar, Type

from requests import Response

from fixtures.api.models.client import CustomRequests, CustomResponse, ErrorBody

logger = logging.getLogger("api")

T = TypeVar("T")


def structure(
    response: Response, type_response: Type[T], body_request: Any = None
) -> CustomResponse[T]:
    url = response.url
    method = response.request.method
    status_code = response.status_code
    request_time = response.elapsed.total_seconds()
    headers = dict(response.request.headers)
    request: CustomRequests = CustomRequests(
        body=body_request, method=method, url=url, headers=headers
    )
    if status_code >= 400:
        body_error = ErrorBody(**response.json())
    else:
        body_error = ErrorBody()
    if 200 <= status_code < 400:
        body = type_response(**response.json())
    else:
        body = None
    custom_response = CustomResponse(
        url=url,
        method=method,
        status_code=status_code,
        body=body,
        request=request,
        request_time=request_time,
        error_body=body_error,
    )
    return custom_response  # type: ignore


def _convert_bytes_to_dict(body: bytes | str | None) -> dict:
    if isinstance(body, bytes):
        return json.loads(body.decode("utf-8"))
    return {}


def _get_field_structure(type_response) -> List:
    """
    Return fields from response type
    """
    fields = []
    for field in type_response.__attrs_attrs__:
        fields.append(field.name)
    return fields


def _get_field_response(response):
    """
    Return fields from response
    """
    try:
        return list(response.json().keys())
    except Exception:
        return response.text
