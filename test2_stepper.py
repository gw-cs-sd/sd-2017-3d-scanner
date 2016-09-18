#/usr/bin/python

from rpi_m542_driver_control import *
import RPi.GPIO as GPIO
import time


#setup pins 
GPIOsetup()


stepClockwise_withAccel(tableSteps/2, speed5)
time.sleep(2.0)
stepCounterClockwise_withAccel(tableSteps/2, speed5)
time.sleep(2.0)

# Test with no acceleration
#step_clockwise(tableSteps/2, speed4)
#time.sleep(2.0)



















file1.close()
GPIO.cleanup()
