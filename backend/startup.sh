#!/bin/bash
python manage.py migrate
gunicorn --bind=0.0.0.0 --workers=4 backend.wsgi