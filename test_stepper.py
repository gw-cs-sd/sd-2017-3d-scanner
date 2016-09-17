#/usr/bin/python

from rpi_m542_driver_control import *
import RPi.GPIO as GPIO
import time


#setup pins 
GPIOsetup()

# Test with no acceleration
#step_clockwise(motorSteps/2, speed4)
#time.sleep(1.0)

#step_clockwise(tableSteps/4, speed4)
#time.sleep(1.0)





#test with acceleration
stepClockwise_withAccel(tableSteps/4+1, speed6) #this does not work yet









#teeth_clockwise(pulleyTeeth, speed4)
#time.sleep(1.0)



file1.close()
GPIO.cleanup()
