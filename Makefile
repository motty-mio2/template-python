format:
	- poetry run ruff . --fix --exit-zero
	- poetry run black .
	- poetry run isort .
	- poetry run mypy . --strict

test:
	poetry run pytest .

api:
	curl localhost:8080/ && curl localhost:8080/name

start:
	docker compose up -d

stop:
	docker compose down
