.PHONY: run, db

run:
	@python src/manage.py runserver

db:
	@docker compose --env-file src/barberq_project/.env up --build -d