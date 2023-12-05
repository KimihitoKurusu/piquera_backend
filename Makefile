# Makefile

.PHONY: install run migrate superuser

install:
	pipenv install

start:
	pipenv run python manage.py runserver

migrate:
	pipenv run python manage.py migrate

superuser:
	pipenv run python manage.py createsuperuser
