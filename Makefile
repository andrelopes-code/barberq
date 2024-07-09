.PHONY: run, db

run:
	@python src/manage.py runserver

db:
	@docker compose --env-file src/core/.env up --build -d

tailwind:
	@npx tailwindcss -i ./src/static/src/input.css -o ./src/static/src/output.css --watch