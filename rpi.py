# Example using RPi.GPIO library to turn on an LED
# Author: Nazmus Nasir
# URL: https://www.EasyProgramming.net

import RPi.GPIO as GPIO
from time import sleep
import sys

inp = sys.argv[1]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = 18

GPIO.setup(led, GPIO.OUT)

# Uncomment the lines below to turn on blink
#while True:
#       GPIO.output(led, GPIO.HIGH)
#       sleep(1)
#       GPIO.output(led, GPIO.LOW)
#       sleep(1)

if inp == "on":
        GPIO.output(led, GPIO.HIGH)
elif inp == "off":
        GPIO.output(led, GPIO.LOW)
else:
        print('Enter "on" or "off" only')
