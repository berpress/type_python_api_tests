import json
import logging
import pprint
from json import JSONDecodeError
from typing import Any, Callable, TypeVar, ParamSpec

from fixtures.api.models.client import CustomResponse


logger = logging.getLogger("api")

T = TypeVar("T")
P = ParamSpec("P")
F = TypeVar("F", bound=Callable[..., Any])
Param = ParamSpec("Param")
RetType = TypeVar("RetType")
OriginalFunc = Callable[..., CustomResponse[T]]
DecoratedFunc = Callable[..., CustomResponse[T]]


def log(message: str) -> Callable[[OriginalFunc], DecoratedFunc]:
    """
    Request Logging
    :return: response
    """

    def wrapper(function: F) -> DecoratedFunc:
        def inner(*args, **kwargs) -> CustomResponse[T]:
            logger.info(message)
            res: CustomResponse = function(*args, **kwargs)
            method = res.method
            assert res.request
            url = res.request.url
            body = res.request.body
            status = res.status_code
            body_sep = " "
            log_request = f"Request method: {method}, url: {url}"
            if body is not None:
                try:
                    json_body = json.dumps(
                        json.loads(body.decode("utf-8")),
                        indent=4,
                        ensure_ascii=False,
                    )
                    if len(body) > 20:
                        body_sep = "\n"
                    log_request += (
                        f", body:{body_sep}{json_body or pprint.pformat(body)}"
                    )
                except AttributeError:
                    log_request += f", body:{body}"
            logger.info(log_request)

            log_response = f"Response method: {method}, url: {url}, status: {status}"
            if res.status_code < 400:
                assert res.body
                body = res.body.dict()
            else:
                body = res.error_body.dict()
            try:
                text_body = str(body)
                if len(text_body) > 20:
                    body_sep = "\n"
                    bd = json.dumps(body, indent=4, ensure_ascii=False)
                    log_response += f", body:{body_sep}{bd}"
                else:
                    log_response += f", body:{json.dumps(body)}"
                logger.info(log_response)
            except JSONDecodeError:
                if len(text_body) > 120:
                    log_response += f", body: {text_body[:120]}..."
                else:
                    log_response += f", body: {text_body}"
                logger.info(log_response)
            return res

        return inner

    return wrapper
