#/usr/bin/python

#run with: sudo python rpi_m542_driver_control.py

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

def pulse_motor():
	#0.002s/pulse = 1 step on motor
	GPIO.output(pulse_pin, 1)
	time.sleep(0.0001)
	GPIO.output(pulse_pin, 0)
	time.sleep(0.0001)

def step_forward(steps):
	GPIO.output(dir_pin, 1)
	for i in range(0, steps):
		pulse_motor()

def step_backward(steps):
	GPIO.output(dir_pin, 0)
	for i in range(0, steps):
		pulse_motor()


step_forward(400)
time.sleep(0.5)
step_backward(400)
time.sleep(0.5)



GPIO.cleanup()
