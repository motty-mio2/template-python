lint:
	poetry run ruff .

format:
	poetry run black .
	poetry run isort .
	poetry run mypy . --strict --platform win32
	poetry run mypy . --strict --platform linux
	poetry run mypy . --strict --platform darwin

test:
	poetry run pytest .

api:
	curl localhost:8080/ && curl localhost:8080/name

