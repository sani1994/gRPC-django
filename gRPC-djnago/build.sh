#!/bin/bash

#python3 -m venv .venv
#source .venv/bin/activate
#pip install -r requirements.txt
python .env
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
