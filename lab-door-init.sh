#! /bin/sh

case "$1" in
  start)
    echo "Starting Lab Door Web Service"
    python /home/pi/Git/lab-door-web/lab-door.py &
    ;;
  stop)
    echo "Stopping Lab Door Web Service"
    killall python
    ;;
esac

exit 0
