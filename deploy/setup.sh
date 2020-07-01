#!/usr/bin/env bash

set -e

PROJECT_GIT_URL='https://github.com/ankit2001/Profile-apis'

PROJECT_BASE_PATH='/usr/local/apps/profiles-rest-api'

echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite supervisor nginx git

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

#mkdir -p $PROJECT_BASE_PATH/env
#python3 -m venv $PROJECT_BASE_PATH/env

pip3 install -r $PROJECT_BASE_PATH/requirements.txt
pip3 install uwsgi==2.0.18

cd $PROJECT_BASE_PATH
python3 manage.py migrate
python3 manage.py collectstatic --noinput

cp $PROJECT_BASE_PATH/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart profiles_api

cp $PROJECT_BASE_PATH/deploy/nginx_profiles_api.conf /etc/nginx/sites-available/profiles_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/profiles_api.conf /etc/nginx/sites-enabled/profiles_api.conf
systemctl restart nginx.service

echo "Lets start"
