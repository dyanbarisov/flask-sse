#!/bin/sh
source venv/bin/activate

flask db migrate
flask db upgrade

redis-server --daemonize yes
exec gunicorn -b :5000 --worker-class gevent --bind 127.0.0.1:8000 notifications:app