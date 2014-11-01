# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO            
from time import sleep               

GPIO.setmode(GPIO.BCM)             
	# нумерация портов через BCM  

GPIO.setup(24, GPIO.OUT)
	# использовать пин 24 для вывода    
  
try:  
    while True:  
        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True
        print "1"  
        sleep(0.5)                 # wait half a second  
        
        GPIO.output(24, 0)         # set GPIO24 to 0/GPIO.LOW/False  
        print "0"
        sleep(0.5)                 # wait half a second  
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program 
