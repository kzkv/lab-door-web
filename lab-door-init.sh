#! /bin/sh

case "$1" in
  start)
    nohup python /home/pi/Git/lab-door-web/lab-door.py > /home/pi/Documents/lab-door.out 2> /home/pi/Documents/lab-door.err < /dev/null &
    ;;
  stop)
    killall python
    ;;
esac

exit 0
