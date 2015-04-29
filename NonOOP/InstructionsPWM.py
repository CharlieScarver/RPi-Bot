import RPi.GPIO as GPIO
from time import *

# --------- Main ---------

def checkForWallInFront():
    
    if pulseFront() > 18.0:
        return False;
    else:
        return True;

def checkForWallOnRight():
    
    if pulseRight() > 18.0:
        return False;
    else:
        return True;


def go():

	Trig1 = 11
	Echo1 = 13
	Trig2 = 7
	Echo2 = 15
	
	#GPIO.add_event_detect(Echo, GPIO.RISING)
        #while not(GPIO.event_detected(Echo)) or frontDistance > 15.0:

        while True:

                wallInFront = checkForWallInFront();
                wallOnRight = checkForWallOnRight();
                                                     
                while wallOnRight and not wallInFront:
                        print("-----f-----");
                        forward(0.3, 100);
                        wallInFront = checkForWallInFront();
                        wallOnRight = checkForWallOnRight();                        
                                
                if wallOnRight:
                        print("-----tlb-----");
                        backward(1);
			#turnLeft(1.5, 100);
                        turn("left-forward", 0.9);
			forward(0.3);
                        turn("left-forward", 1.5);
                        forward(1);
                        turn("left-forward", 1);
			#backward(0.5);
  			#turn("left-forward", 0.3);
                        #print("Here");

                        wallInFront = checkForWallInFront();
                        wallOnRight = checkForWallOnRight();
                                        
                        while wallInFront or not wallOnRight:
                                print("-----tl-----");
                                turnLeft(0.3, 100);
                                forward(0.3, 100);
                                turnLeft(0.3, 100);
                                backward(0.3, 100);
                                wallInFront = checkForWallInFront();
                                wallOnRight = checkForWallOnRight();
            
                else:
                        print("-----trb-----");
                        #backward(1);
                        #turn("right-forward", 1.5, 100);
                        #forward(1, 100);
                        #turn("right-forward", 1.5, 100);
                        #backward(0.5, 100);
                        #turn("right-forward", 0.8, 100);
               		forward(0.1);
                        turnRight(2);
                        backward(0.3);
			turnRight(1.5);
			forward(3);
                        #turnRight(1.5);
                        #forward(2);
                        #print("There");

                        wallOnRight = checkForWallOnRight();
			wallInFront = checkForWallInFront();
                                       
                        while not wallOnRight and not wallInFront:
                                print("-----tr-----");
                                turnRight(0.3, 100);
                                forward(0.3, 100);
                                wallOnRight = checkForWallOnRight();
				wallInFront = checkForWallInFront();
	
                                
                print "End of cycle"


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

	#print "Going forward"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

        # GPIO.PWM(pin, frequency)
	# frequency in Hz 
	p1 = GPIO.PWM(Motor1E, 100)
	p2 = GPIO.PWM(Motor2E, 100)
	
        p1.start(dutyCycle);
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

	#print "Going backward"
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

	#print "Turning right"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)

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

	#print "Turning left"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

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

def turn(direction, duration = 3.8, dutyCycle = 100):
        # directions: right-forward, right backward, left-forward, left-backward
        # duration in seconds
        # dutyCycle between 0.0% and 100.0%

	Motor1A = 16
	Motor1B = 18
	Motor1E = 22

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19

        if direction == "right-forward":
                GPIO.output(Motor1A,GPIO.HIGH)
                GPIO.output(Motor1B,GPIO.LOW)

                GPIO.output(Motor2A,GPIO.LOW)
                GPIO.output(Motor2B,GPIO.HIGH)

                # GPIO.PWM(pin, frequency)
                # frequency in Hz 
                p1 = GPIO.PWM(Motor1E, 100)
                p2 = GPIO.PWM(Motor2E, 100)
	
                p1.start(dutyCycle/5.0)
                p2.start(dutyCycle)
                
        elif direction == "left-forward":
                GPIO.output(Motor1A,GPIO.LOW)
                GPIO.output(Motor1B,GPIO.HIGH)

                GPIO.output(Motor2A,GPIO.HIGH)
                GPIO.output(Motor2B,GPIO.LOW)

                p1 = GPIO.PWM(Motor1E, 100)
                p2 = GPIO.PWM(Motor2E, 100)
	
                p1.start(dutyCycle)
                p2.start(dutyCycle/5.0)

        sleep(duration)

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

        sleep(2);
        

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

        print "Front Distance", distance, "cm"

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

        print "Right Distance", distance, "cm"

        return distance



