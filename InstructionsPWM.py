import RPi.GPIO as GPIO
from time import sleep

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

def forward(duration, dutyCycle = 100):
        # duration in seconds
        # dutyCycle between 0.0% and 100.0%

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19

	print "Going forward"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)

	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

        # GPIO.PWM(pin, frequency)
	# frequency in Hz 
	p1 = GPIO.PWM(Motor1E, 100)
	p2 = GPIO.PWM(Motor2E, 100)
	
        p1.start(dutyCycle)
	p2.start(dutyCycle)

	# p.ChangeDutyCycle(90)
        # p.ChangeFrequency(100)

	sleep(duration)

	print "Stopping"
	p1.stop()
	p2.stop()

def backward(duration, dutyCycle = 100):

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19

	print "Going backward"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

        p1 = GPIO.PWM(Motor1E, 100)
	p2 = GPIO.PWM(Motor2E, 100)
	
        p1.start(dutyCycle)
	p2.start(dutyCycle) # 25

	sleep(duration)

	print "Stopping"
	p1.stop()
	p2.stop()
	

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



