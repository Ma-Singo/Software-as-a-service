#!/bin/sh

echo "Applying data migration"
python3 manage.py migrate

exec "$@"