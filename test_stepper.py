#/usr/bin/python

from rpi_m542_driver_control import *
import RPi.GPIO as GPIO
import time


#setup pins 
GPIOsetup()

#test
step_forward(motorSteps/2, speed6)
time.sleep(0.5)

teeth_backward(pulleyTeeth, speed4)
time.sleep(0.5)



file1.close()
GPIO.cleanup()
