#!/bin/bash

APP_NAME="user-manager"
SERVICES_PATH="/etc/init.d/"
APP_PATH="/usr/local/$APP_NAME"

rm -Rf "$APP_PATH"

echo "Coping files ..."
cp -pR "$APP_NAME.sh" "$SERVICES_PATH"
chown $USER:$USER "$SERVICES_PATH""$APP_NAME.sh"
chmod +x "$SERVICES_PATH""$APP_NAME.sh"

mkdir -p "$APP_PATH"
cp -pR app "$APP_PATH"/app
cp -pR run.pyc "$APP_PATH"/run.pyc

update-rc.d "$APP_NAME.sh" defaults

DATA_BASE="$APP_PATH"/"$APP_NAME.db"
echo "Creating database $DATA_BASE ..."
/usr/bin/python db.pyc --database "$DATA_BASE"

service $APP_NAME stop

echo "Start service: sudo service $APP_NAME start ..."
