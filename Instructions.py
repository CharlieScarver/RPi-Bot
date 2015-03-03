import RPi.GPIO as GPIO
from time import *

def getReady():
	
	GPIO.setmode(GPIO.BOARD)

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19

	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)

	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor2B,GPIO.OUT)
	GPIO.setup(Motor2E,GPIO.OUT)

def clean():
	
	GPIO.cleanup()

def forward(n):

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19

	print "Going forward"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)

	sleep(n)

	print "Stopping"
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)

def backward(n):

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19

	print "Going backward"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)

	sleep(n)

	print "Stopping"
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)

def turnRight(n):

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	print "Turning right"
	GPIO.output(Motor1A, GPIO.HIGH)
	GPIO.output(Motor1B, GPIO.LOW)
	GPIO.output(Motor1E, GPIO.HIGH)

	sleep(n)

	GPIO.output(Motor1E, GPIO.LOW)

def turnLeft(n):

	Motor1A = 23
	Motor1B = 21
	Motor1E = 19

	print "Turning left"
	GPIO.output(Motor1A, GPIO.LOW)
	GPIO.output(Motor1B, GPIO.HIGH)
	GPIO.output(Motor1E, GPIO.HIGH)

	sleep(n)

	GPIO.output(Motor1E, GPIO.LOW)

def stop():
        
        Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19
	
        print "Stopping"
        GPIO.output(Motor1A, GPIO.LOW)
	GPIO.output(Motor1B, GPIO.LOW)
	GPIO.output(Motor1E, GPIO.LOW)
	
	GPIO.output(Motor2A, GPIO.LOW)
	GPIO.output(Motor2B, GPIO.LOW)
	GPIO.output(Motor2E, GPIO.LOW)


def getSensorsReady():

        GPIO.setmode(GPIO.BOARD)

	Trig1 = 11
	Echo1 = 13
	Trig2 = 7
	Echo2 = 15

        print "Getting sensors ready"
	GPIO.setup(Trig1,GPIO.OUT)
	GPIO.setup(Echo1,GPIO.IN)

	GPIO.setup(Trig2,GPIO.OUT)
	GPIO.setup(Echo2,GPIO.IN)

	GPIO.output(Trig1, False)
        GPIO.output(Trig2, False)
        

def pulse1():

        Trig = 11
        Echo = 13

        GPIO.output(Trig, False)
        print "Sensor settling"
        sleep(0.01)

        GPIO.output(Trig, True)
        sleep(0.00001)        
        GPIO.output(Trig, False)

        while GPIO.input(Echo) == 0:
                pulse_start = time()

        while GPIO.input(Echo) == 1:
                pulse_end = time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        print "Distance", distance, "cm"

        return distance


def pulse2():

        Trig = 7
        Echo = 15

        GPIO.output(Trig, False)
        print "Sensor settling"
        sleep(0.01)

        GPIO.output(Trig, True)
        sleep(0.00001)        
        GPIO.output(Trig, False)

        while GPIO.input(Echo) == 0:
                pulse_start = time()

        while GPIO.input(Echo) == 1:
                pulse_end = time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        print "Distance", distance, "cm"

        return distance


def go():

	Trig1 = 11
	Echo1 = 13
	Trig2 = 7
	Echo2 = 15
	
	#GPIO.add_event_detect(Echo, GPIO.RISING)
        #while not(GPIO.event_detected(Echo)) or frontDistance > 15.0:

        while True:

                frontDistance = pulse1()
                if pulse2() > 15.0:
                        wallOnRight = False
                else:
                        wallOnRight = True
                                                     
                while wallOnRight and frontDistance > 15.0:
                        forward(0.3)
                        frontDistance = pulse1()
                        if pulse2() > 15.0:
                                wallOnRight = False
                        else:
                                wallOnRight = True
                
                if wallOnRight:
                        turnLeft(1)
                        backward(0.6)
                else:
                        turnRight(1)
                        backward(0.6)



