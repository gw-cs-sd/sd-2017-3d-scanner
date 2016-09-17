#/usr/bin/python

from rpi_m542_driver_control import *
import RPi.GPIO as GPIO
import time


#setup pins 
GPIOsetup()

#test
#step_clockwise(motorSteps/2, speed6)
#time.sleep(1.0)

stepClockwise_accel(tableSteps/4, speed4)

#step_clockwise(tableSteps, speed4)
time.sleep(1.0)

#teeth_clockwise(pulleyTeeth, speed4)
#time.sleep(1.0)



file1.close()
GPIO.cleanup()
