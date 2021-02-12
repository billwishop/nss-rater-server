#!/bin/bash

rm -rf raterapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations raterapi
python manage.py migrate raterapi
python manage.py loaddata user
python manage.py loaddata token
python manage.py loaddata gamer
python manage.py loaddata game
python manage.py loaddata category
python manage.py loaddata game_category
# python manage.py loaddata image
# python manage.py loaddata rating
python manage.py loaddata review
