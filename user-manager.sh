#! /bin/sh

### BEGIN INIT INFO
# Provides:          user-manager
# Required-Start:    $remote_fs $network $named $time
# Required-Stop:     $remote_fs $network $named $time
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Starts user-manager server
# Description:       Starts user-manager server, an user manager api
#                    written in Python.
### END INIT INFO

PORT=5007
HOST='"0.0.0.0"'

APP_NAME="user-manager"
APP_PATH="/usr/local/$APP_NAME"
SCRIPT="/usr/bin/python $APP_PATH/run.pyc --port=$PORT --host=$HOST"
PIDFILE="/var/run/$APP_NAME.pid"
LOGFILE="/var/log/$APP_NAME.log"

export UM_DATABASE="$APP_PATH"/"$APP_NAME.db"

start() {
  
  if [ -f "$PIDFILE" ] && kill -0 $(cat "$PIDFILE"); then
    echo "Service already running" >&2
    echo "Process: $( cat $PIDFILE )"
    return 1
  fi

  echo "Starting service …" >&2
  CMD="$SCRIPT &> $LOGFILE & echo \$!"
  su -c "$CMD" "$USER" > "$PIDFILE"
  echo "Service started on port $PORT" >&2
  echo "Process: $( cat $PIDFILE )"

}

stop() {
  
  if [ ! -f "$PIDFILE" ] || ! kill -0 $(cat "$PIDFILE"); then
    echo "Service not running" >&2
    return 1
  fi
  
  echo "Stopping service…" >&2
  echo "Process: $(cat $PIDFILE)"

  kill -9 $(cat "$PIDFILE")
  rm -f "$PIDFILE"
  echo "Service stopped" >&2

}

uninstall() {
  echo -n "Are you really sure you want to uninstall this service? That cannot be undone. [yes|No] "
  read SURE
  if [ "$SURE" = "yes" ]; then
    stop
    rm -f "$PIDFILE"
    echo "Notice: log file is not going to be removed: '$LOGFILE'" >&2
    update-rc.d -f "$APP_NAME" remove
    rm -fv "$0"
  fi
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  uninstall)
    uninstall
    ;;
  restart)
    stop
    start
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|uninstall}"
esac