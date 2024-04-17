# type_python_api_tests
Python API tests with strong typing

In this repository will use such key libraries/technologies

* Python 3.10
* Mypy (Static Typing for Python) https://github.com/python/mypy
* Pydantic (Data validation and settings management using Python type annotations) https://docs.pydantic.dev/
* Black (Code formatter) https://pypi.org/project/black/
* Type hints https://docs.python.org/3/library/typing.html
* pytest (Testing tool) https://docs.pytest.org/en/7.3.x/
* poetry (Dependency manager for Python projects)

## How to start

Use docker
```
docker run -d -p 5000:5000 litovsky/flask-api-test
```
And check in browser

```
http://localhost:56733/

# you will see

{
"GitHub": "https://github.com/berpress/flask-restful-api",
"swagger": "https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0"
}

# its ok
```

How are you?
