#/usr/bin/python

#run with: sudo python test_stepper.py

# April 28, 2016
# Karl Preisner, Bob Forcha

# 1. This is the setup for the Nema 23 stepper motor with M542T Driver. 
# 2. After each stepper movement call, the relative location of the stepper motor, in teeth with repsect to the gear, is written to a file. 
# 3. Move by step or by tooth

# TODO: attach a hall sensor to the arm and a fixed location on the table. Call an initialization() method that scans the entire the table. When the hall sensor is triggered, carefully stop the arm and slowly back up until the hall sensors are lined up again. This location will be fixed and will be tooth 0. 

import RPi.GPIO as GPIO
import time
from sys import argv



#initialize() #TODO: write this method 


# global variables
moveCount = -1 # tracker number for movements
location = 0  # current location

# GPIO pin assignments
pulse_pin = 23
dir_pin = 24
ena_pin = 25

def GPIOsetup():
	# GPIO settings
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(pulse_pin, GPIO.OUT)
	GPIO.setup(dir_pin, GPIO.OUT)
	GPIO.setup(ena_pin, GPIO.OUT)

	GPIO.output(ena_pin, 0)
	GPIO.output(pulse_pin, 0)
	GPIO.output(dir_pin, 0)



# Significant numbers for calculations
motorSteps = 400 # number of steps for 1 cycle of the motor
pulleyTeeth = 40 # number of teeth on the pulley
tableTeeth = 300 # number of teeth on the table gear
stepsPerTooth = motorSteps / pulleyTeeth # = 10 steps
tableSteps = tableTeeth * stepsPerTooth  # = 120000 steps
motorCyclesPerArmCycle = 300/40          # = 7.5 motor cycles


#Speeds
speed1 = 0.01  #1 step = 0.02s, 1 rev motor/pulley (400 steps/40 teeth) = 8.0s, 1 rev arm (300 teeth) = 60s
speed2 = 0.008 #1 step = 0.016s, 1 rev motor/pulley (400 steps/40 teeth) = 6.4s, 1 rev arm (300 teeth) = 48s
speed3 = 0.006 #1 step = 0.012s, 1 rev motor/pulley (400 steps/40 teeth) = 4.8s, 1 rev arm (300 teeth) = 36s
speed4 = 0.004 #1 step = 0.008s, 1 rev motor/pulley (400 steps/40 teeth) = 3.2s, 1 rev arm (300 teeth) = 24s
speed5 = 0.002 #1 step = 0.004s, 1 rev motor/pulley (400 steps/40 teeth) = 1.6s, 1 rev arm (300 teeth) = 12s
speed6 = 0.001 #1 step = 0.002s, 1 rev motor/pulley (400 steps/40 teeth) = 0.8s, 1 rev arm (300 teeth) = 6s





#this function is used for all step functions
def pulse_motor(speed):
	#speed*2/pulse = 1 step on motor
	GPIO.output(pulse_pin, 1)
	time.sleep(speed)
	GPIO.output(pulse_pin, 0)
	time.sleep(speed)

# writes the relative tooth location of the arm with respect to the table gear
def trackLocation(teeth, direction):
	global moveCount
	moveCount += 1
	if direction == "forward":
		global location
		location += + teeth
		location %= tableTeeth
	else:
		if direction == "backward":
			location -= teeth
			location %= tableTeeth
			if location < 0:
				location += tableTeeth
	file1.write(str(moveCount) + ": Location = " + str(location) + "\n")





# movement by motor step
# step_forward
def step_forward(steps, speed):  
	GPIO.output(dir_pin, 1)
	for i in range(0, steps):
		pulse_motor(speed)
	trackLocation(steps/stepsPerTooth, "forward")

# step_backward
def step_backward(steps, speed): 
	GPIO.output(dir_pin, 0)
	for i in range(0, steps):
		pulse_motor(speed)
	trackLocation(steps/stepsPerTooth, "backward")

# movement by number of teeth
# teeth_forward
def teeth_forward(teeth, speed):
	GPIO.output(dir_pin, 1)
	for i in range(0, teeth * stepsPerTooth):
		pulse_motor(speed)
	trackLocation(teeth, "forward")

# teeth_backward
def teeth_backward(teeth, speed):
	GPIO.output(dir_pin, 0)
	for i in range(0, teeth * stepsPerTooth):
		pulse_motor(speed)
	trackLocation(teeth, "backward")







# write to file the locations of the stepper in this test
filename = "relativeStepperLocation.txt"
print("   writing file: " + filename) #This file keeps track of the relative location of the stepper motor in this session.
file1 = open(filename, 'w')
file1.truncate()
file1.write("This file contains relative location for the current session of the stepper motor\n\n")
trackLocation(0, "forward")

