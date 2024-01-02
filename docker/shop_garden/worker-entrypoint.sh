#!/bin/sh

until cd /app/shop_garden
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A celery_app.app worker -B --loglevel=info
