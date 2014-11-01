# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO

from time import sleep

from flask import Flask
app = Flask(__name__)
    # веб-сервис Фласка

GPIO.setmode(GPIO.BCM)             
    # нумерация портов через BCM  

GPIO.setup(24, GPIO.OUT)
    # использовать пин 24 для вывода    


@app.route("/")
def root():
   templateData = {
      'title' : 'Lab Door Control',
      }
   return render_template('index.html', **templateData)
   

@app.route("/open")
def openDoor():
    GPIO.output(24, True)
    sleep(1)
    GPIO.output(24, False)
        
    message = "GPIO24 ON"
    templateData = {
    }
    return message

