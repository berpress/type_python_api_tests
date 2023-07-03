import logging
import pytest

from fixtures.api_client import ClientApi

logger = logging.getLogger("api")


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="http://127.0.0.1:5000",
    ),
    parser.addoption(
        "--swagger-url",
        action="store",
        help="enter swagger url",
        default="https://api.swaggerhub.com/apis/berpress/flask-rest-api/1.0.0",
    )


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start api tests, url is {url}")
    return ClientApi(url=url)
