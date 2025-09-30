.PHONY: run worker format lint migrate

run:
	uvicorn app.main:app --reload

worker:
	python -m app.worker.outbox_worker

format:
	black app

lint:
	ruff check app

migrate:
	alembic upgrade head
