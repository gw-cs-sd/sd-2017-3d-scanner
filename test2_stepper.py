#/usr/bin/python

from rpi_m542_driver_control import *
import RPi.GPIO as GPIO
import time


#setup pins 
GPIOsetup()

#test
step_forward(400, 0.001)
time.sleep(0.5)

degree_forward(360, 0.001)




GPIO.cleanup()
