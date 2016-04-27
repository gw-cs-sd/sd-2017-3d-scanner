#/usr/bin/python

from rpi_m542_driver_control import *
import rpi_m542_driver_control as motor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pulse_pin = 23
dir_pin = 24
ena_pin = 25

GPIO.setup(pulse_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(ena_pin, GPIO.OUT)

GPIO.output(ena_pin, 0)
GPIO.output(pulse_pin, 0)
GPIO.output(dir_pin, 0)

#Speeds
speed1 = 0.01 #1 step = 0.02s, 1 rev motor/pulley (400 steps/40 teeth) = 8s,1 rev belt (500 teeth) = 100s

speed2 = 0.008 #1 step = 0.016s, 1 rev motor/pulley (400 steps/40 teeth) = 6.4s, 1 rev belt (500 teeth) = 80s

speed3 = 0.006 #1 step = 0.012s, 1 rev motor/pulley (400 steps/40 teeth) = 4.8s, 1 rev belt (500 teeth) = 60s

speed4 = 0.004 #1 step = 0.008s, 1 rev motor/pulley (400 steps/40 teeth) = 3.2s, 1 rev belt (500 teeth) = 40s

speed5 = 0.002 #1 step = 0.004s, 1 rev motor/pulley (400 steps/40 teeth) = 1.6s, 1 rev belt (500 teeth) = 20s





#test
motor.step_forward(400, speed5)






GPIO.cleanup()
