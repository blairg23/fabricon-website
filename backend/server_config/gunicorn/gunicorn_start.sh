#!/bin/bash

NAME="fabricon"                                     #Name of the application (*)
DJANGODIR=/var/www/html/fabricon-website/backend    # Django project directory (*)
SOCKFILE=/var/www/html/run/gunicorn.sock            # we will communicate using this unix socket (*)
USER=root                                           # the user to run as (*)
GROUP=webdata                                       # the group to run as (*)
NUM_WORKERS=1                                       # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=server.settings              # which settings file should Django use (*)
DJANGO_WSGI_MODULE=server.wsgi                      # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source ~/.virtualenvs/fabricon/bin/activate
pip3 install -r requirements.txt --upgrade
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE