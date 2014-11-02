#! /bin/sh

case "$1" in
  start)
    nohup python /home/pi/Git/lab-door-web/lab-door.py &
    ;;
  stop)
    killall python
    ;;
esac

exit 0
