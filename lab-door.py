# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO

import atexit
    # модуль для вызовов во время выключения интерпретатора

from time import sleep

from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

atexit.register(GPIO.cleanup)
    # клин-ап портов во время выхода
