#!/usr/bin/env bash

# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python core/manage.py migrate --database=production
python core/manage.py collectstatic --no-input
python core/manage.py loaddata data.json