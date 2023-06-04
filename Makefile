lint:
	@pre-commit run --all-files

test:
	@pytest tests/api -q

mypy:
    mypy .
