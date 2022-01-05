#!/bin/sh

# Start Gunicorn processes
echo Starting Gunicorn

# run the created app from run.py
# bind to this port
# how many threads to create
exec gunicorn --chdir ./server run:app --name sw_rpg_manager --bind 0.0.0.0:5100 --worker-class gevent --workers 3
