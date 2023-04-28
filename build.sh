#!/usr/bin/env bash

# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py migrate --database=production
python manage.py collectstatic --no-input
python manage.py loaddata data.json