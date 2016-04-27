#/usr/bin/python

#run with: sudo python rpi_m542_driver_control.py

import RPi.GPIO as GPIO
import time

pulse_pin = 23
dir_pin = 24
ena_pin = 25

def GPIOsetup():
	#pins on raspberry pi
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(pulse_pin, GPIO.OUT)
	GPIO.setup(dir_pin, GPIO.OUT)
	GPIO.setup(ena_pin, GPIO.OUT)

	GPIO.output(ena_pin, 0)
	GPIO.output(pulse_pin, 0)
	GPIO.output(dir_pin, 0)



#Significant numbers for calculations
motorCycleSteps = 400 #steps for 1 revolution of the motor
pulleyTeeth = 40
beltTeeth = 500

beltCycleSteps = beltTeeth / pulleyTeeth * motorCycleSteps #number of steps to make a full cycle with the timing belt

stepsPerTooth = motorCycleSteps / pulleyTeeth # = 10 steps


teethPerDegree = beltTeeth / 360.0
stepsPerDegree = teethPerDegree * stepsPerTooth
print(teethPerDegree)
print(stepsPerDegree)

#Speeds
speed1 = 0.01 #1 step = 0.02s, 1 rev motor/pulley (400 steps/40 teeth) = 8s,1 rev belt (500 teeth) = 100s

speed2 = 0.008 #1 step = 0.016s, 1 rev motor/pulley (400 steps/40 teeth) = 6.4s, 1 rev belt (500 teeth) = 80s

speed3 = 0.006 #1 step = 0.012s, 1 rev motor/pulley (400 steps/40 teeth) = 4.8s, 1 rev belt (500 teeth) = 60s

speed4 = 0.004 #1 step = 0.008s, 1 rev motor/pulley (400 steps/40 teeth) = 3.2s, 1 rev belt (500 teeth) = 40s

speed5 = 0.002 #1 step = 0.004s, 1 rev motor/pulley (400 steps/40 teeth) = 1.6s, 1 rev belt (500 teeth) = 20s





#this function is used for all step functions
def pulse_motor(speed):
	#0.02s/pulse = 1 step on motor
	GPIO.output(pulse_pin, 1)
	time.sleep(speed)
	GPIO.output(pulse_pin, 0)
	time.sleep(speed)

#movement by motor step
def step_forward(steps, speed):
	GPIO.output(dir_pin, 1)
	for i in range(0, steps):
		pulse_motor(speed)

def step_backward(steps, speed):
	GPIO.output(dir_pin, 0)
	for i in range(0, steps):
		pulse_motor(speed)



#movement by degree of arm with repsect to table
def degree_forward(degree, speed):
	GPIO.output(dir_pin, 1)
	for i in range(0, degree * stepsPerDegree):
		pulse_motor(speed)

def degree_backward(degree, speed):
	GPIO.output(dir_pin, 0)
	for i in range(0, degree * stepsPerDegree):
		pulse_motor(speed)



