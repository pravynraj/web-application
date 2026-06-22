#!/bin/bash
# wait for postgres to be ready
echo "Waiting for PostgreSQL to start..."
while ! pg_isready -h db -U $POSTGRES_USER; do
  sleep 1
done
echo "PostgreSQL started"

# Run migrations
echo "Running database migrations..."
flask db upgrade

# Start Gunicorn server
echo "Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:5000 "run:app"
