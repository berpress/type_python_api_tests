# import json
# import logging
# import pprint
# import warnings
# from functools import wraps
# from json import JSONDecodeError
# from typing import Any, Callable, TypeVar
#
# from requests import Response
#
#
# F = TypeVar("F", bound=Callable[..., Any])
#
# logger = logging.getLogger("ncps")
#
#
# def log(message: str):
#     """
#     Request Logging
#     :return: response
#     """
#
#     def wrapper(function: F) -> F:
#         @wraps(function)
#         def inner(*args, **kwargs) -> Response:
#             logger.info(message)
#             res = function(*args, **kwargs)
#             is_log = kwargs.get("is_log")
#             if is_log is True or is_log is None:
#                 method = res.request.method
#                 url = res.request.url
#                 body = res.request.body
#                 status = res.status_code
#                 body_sep = " "
#                 log_request = f"Request method: {method}, url: {url}"
#                 if body is not None:
#                     try:
#                         json_body = json.dumps(
#                             json.loads(body.decode("utf-8")),
#                             indent=4,
#                             ensure_ascii=False,
#                         )
#                         if len(body) > 20:
#                             body_sep = "\n"
#                         log_request += (
#                             f", body:{body_sep}{json_body or pprint.pformat(body)}"
#                         )
#                     except AttributeError:
#                         log_request += f", body:{body}"
#                 logger.info(log_request)
#
#                 log_response = (
#                     f"Response method: {method}, url: {url}, status: {status}"
#                 )
#                 try:
#                     body = res.json()
#                     if len(res.content) > 20:
#                         body_sep = "\n"
#                         bd = json.dumps(body, indent=4, ensure_ascii=False)
#                         log_response += f", body:{body_sep}{bd}"
#                     else:
#                         log_response += f", body:{json.dumps(body)}"
#                     logger.info(log_response)
#                 except JSONDecodeError:
#                     if len(res.text) > 120:
#                         log_response += f", body: {res.text[:120]}..."
#                     else:
#                         log_response += f", body: {res.text}"
#                     logger.info(log_response)
#             return res
#
#         return inner
#
#     return wrapper
#
#
# def clear_after_request(func):
#     def wrapper(*args, **kwargs):
#         logger.info("Clear after request")
#         client = Client()
#         res = func(*args, **kwargs)
#         client.clear_after_run()
#         return res
#
#     return wrapper
#
#
# def deprecated(message: str):
#     def wrapper(function: F) -> F:
#         @wraps(function)
#         def inner(*args, **kwargs):
#             warnings.simplefilter("always", DeprecationWarning)  # turn off filter
#             warnings.warn(
#                 "Call to deprecated function {} (reason: {}).".format(
#                     function.__name__, message
#                 ),
#                 category=DeprecationWarning,
#                 stacklevel=2,
#             )
#             warnings.simplefilter("default", DeprecationWarning)  # reset filter
#             return function(*args, **kwargs)
#
#         return inner
#
#     return wrapper
