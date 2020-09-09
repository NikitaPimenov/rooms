#!/bin/bash

systemctl stop dorm
poetry install
poetry run dorm_server/manage.py migrate
poetry run dorm_server/manage.py collectstatic -c --noinput
poetry run dorm_server/manage.py check --deploy
systemctl start dorm
