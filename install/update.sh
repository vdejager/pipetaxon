#!/bin/bash

python manage.py migrate

python manage.py get_taxonomy
python manage.py build_database --taxonomy data/taxonomy
python manage.py build_database --lineage data/taxonomy
