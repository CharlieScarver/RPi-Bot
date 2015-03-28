import RPi.GPIO as GPIO
from time import *


# --------- Cleanup ---------

def clean():
	GPIO.cleanup()

# --------- Basic Movement --------- 

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

def forward(duration = 2, dutyCycle = 100):
        # duration in seconds
        # dutyCycle between 0.0% and 100.0%

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19

	print "Going forward"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

        # GPIO.PWM(pin, frequency)
	# frequency in Hz 
	p1 = GPIO.PWM(Motor1E, 100)
	p2 = GPIO.PWM(Motor2E, 100)
	
        p1.start(dutyCycle)
	p2.start(dutyCycle)

	# p.ChangeDutyCycle(90)
        # p.ChangeFrequency(100)

	sleep(duration)

	#print "Stopping"
	p1.stop()
	p2.stop()

	sleep(0.05)

def backward(duration = 2, dutyCycle = 100):

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19

	print "Going backward"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)

	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

        p1 = GPIO.PWM(Motor1E, 100)
	p2 = GPIO.PWM(Motor2E, 100)
	
        p1.start(dutyCycle)
	p2.start(dutyCycle) # 25

	sleep(duration)

	#print "Stopping"
	p1.stop()
	p2.stop()

	sleep(0.05)

def turnRight(duration = 3.8, dutyCycle = 100):
        # duration in seconds
        # dutyCycle between 0.0% and 100.0%

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19

	print "Turning right"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

        # GPIO.PWM(pin, frequency)
	# frequency in Hz 
	p1 = GPIO.PWM(Motor1E, 100)
	p2 = GPIO.PWM(Motor2E, 100)
	
        p1.start(dutyCycle/5.0)
	p2.start(dutyCycle)

	sleep(duration)

	#print "Stopping"
	p1.stop()
	p2.stop()

	sleep(0.05)

def turnLeft(duration = 3.8, dutyCycle = 100):
        # duration in seconds
        # dutyCycle between 0.0% and 100.0%

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19

	print "Turning left"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

        # GPIO.PWM(pin, frequency)
	# frequency in Hz 
	p1 = GPIO.PWM(Motor1E, 100)
	p2 = GPIO.PWM(Motor2E, 100)
	
        p1.start(dutyCycle)
	p2.start(dutyCycle/5.0)

	sleep(duration)

	#print "Stopping"
	p1.stop()
	p2.stop()

	sleep(0.05)

def myStop():
        
        Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19
	
        print "Stopping here"
        GPIO.output(Motor1A, GPIO.LOW)
	GPIO.output(Motor1B, GPIO.LOW)
	
	GPIO.output(Motor2A, GPIO.LOW)
	GPIO.output(Motor2B, GPIO.LOW)

	p1 = GPIO.PWM(Motor1E, 100)
	p2 = GPIO.PWM(Motor2E, 100)
	
        p1.start(0)
        p2.start(0)

        sleep(0.1)

	p1.stop()
	p2.stop()


# --------- Sensors --------- 

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
        

def pulseFront():

        Trig = 11
        Echo = 13

        GPIO.output(Trig, False)
        #print "Sensor settling"
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


def pulseRight():

        Trig = 7
        Echo = 15

        GPIO.output(Trig, False)
        #print "Sensor settling"
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

# --------- Main --------- 

def go():

	Trig1 = 11
	Echo1 = 13
	Trig2 = 7
	Echo2 = 15
	
	#GPIO.add_event_detect(Echo, GPIO.RISING)
        #while not(GPIO.event_detected(Echo)) or frontDistance > 15.0:

        while True:

                frontDistance = pulseFront()
                if pulseRight() > 15.0:
                        wallOnRight = False
                else:
                        wallOnRight = True
                                                     
                while wallOnRight and frontDistance > 15.0:
                        print "-----f-----"
                        forward(0.3, 100)
                        frontDistance = pulseFront()
                        if pulseRight() > 15.0:
                                wallOnRight = False
                        else:
                                wallOnRight = True     
                if wallOnRight:
                        turnLeft(2, 100)
                        backward(0.5, 100)
                        turnLeft(2, 100)
                        backward(2, 100)
                        turnLeft(2, 100)
                        print "Here"
                        forward(1, 100)

                        frontDistance = pulseFront()
                        if pulseRight() > 15.0:
                                wallOnRight = False
                        else:
                                wallOnRight = True
                                        
                        while not frontDistance > 15.0 and wallOnRight:
                                print "-----tl-----"
                                turnLeft(0.3, 100)
                                forward(0.3, 100)

                                frontDistance = pulseFront()
                                if pulseRight() > 15.0:
                                        wallOnRight = False
                                else:
                                        wallOnRight = True             
                else:
                        turnRight(2, 100)
                        backward(0.5, 100)
                        turnRight(2, 100)
                        backward(2, 100)
                        turnRight(2, 100)
                        print "There"
                        forward(1, 100)

                        frontDistance = pulseFront()
                        if pulseRight() > 15.0:
                                wallOnRight = False
                        else:
                                wallOnRight = True
                                        
                        while not wallOnRight and frontDistance > 15.0:
                                print "-----tr-----"
                                turnRight(0.3, 100)
                                forward(0.3, 100)

                                frontDistance = pulseFront()
                                if pulseRight() > 15.0:
                                        wallOnRight = False
                                else:
                                        wallOnRight = True
                print "End of cycle"
                                    


