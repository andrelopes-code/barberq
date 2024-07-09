.PHONY: run, db, cov, test, tailwind

run:
	@python src/manage.py runserver

db:
	@docker compose --env-file src/core/.env up --build -d

tailwind:
	@npx tailwindcss -i ./src/static/src/input.css -o ./src/static/src/output.css --watch

test:
	@cd src ; python manage.py test barberq

cov:
	@cd src ; coverage run manage.py test barberq && coverage report && coverage html