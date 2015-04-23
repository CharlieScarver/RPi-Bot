import RPi.GPIO as GPIO
from time import *


class PiBot:

    name = 'PiBot'

    # Pins
    M1A = 16
    M2B = 18
    M1E = 22
    
    M2A = 23
    M2B = 21
    M2E = 19

    S1T = 11
    S1E = 13

    S2T = 7
    S2E = 15

    # Max Speed/DutyCycle
    MAX_SPEED = 100

    # Settle and Move Durations
    MOTOR_SETTLE_DUR = 0.03

    SENSOR_SETTLE_DUR = 2.00

    MOVE_DUR_PER_TICK = 0.3

    # Wall Detection Distances

    FRONT_WALL_DET_DIST = 15.0

    RIGHT_WALL_DET_DIST = 15.0

    # --------- Constructor ---------

    def __init__(self, newName):
        self.name = newName

    # --------- Main ---------

    def frontWallCheck(self):

        frontDist = pulseFront()
        
        if frontDist > self.FRONT_WALL_DET_DIST:
            return [False, frontDist]
        else:
            return [True, frontDist]

    def rightWallCheck(self):

        rightDist = pulseRight()
        
        if rightDist > self.RIGHT_WALL_DET_DIST:
            return [False, rightDist]
        else:
            return [True, rightDist]


    def go(self):

        lastDistsRight[15.0, 15.0, 15.0];

        while True:

            frontCheckResult = frontWallCheck()
            wallInFront = frontCheckResult
            wallOnRight = rightWallCheck()

            lastDistsRight[0] = rightWallCheck()
                                                         
            while wallOnRight and not wallInFront:
                print("-----f-----")
                forward(self.MOVE_DUR_PER_TICK, self.MAX_SPEED)
                wallInFront = frontWallCheck()
                wallOnRight = rightWallCheck()

                
            
                                    
                print("End of cycle")


    # --------- Cleanup ---------
    def clean(self):
            GPIO.cleanup()

    # --------- Basic Movement --------- 

    def getReady(self):
            
            GPIO.setmode(GPIO.BOARD)

            GPIO.setup(self.M1A, GPIO.OUT)
            GPIO.setup(self.M1B, GPIO.OUT)
            GPIO.setup(self.M1E, GPIO.OUT)

            GPIO.setup(self.M2A, GPIO.OUT)
            GPIO.setup(self.M2B, GPIO.OUT)
            GPIO.setup(self.M2E, GPIO.OUT)

    def forward(self, duration = 2, dutyCycle = 100):
            # duration in seconds
            # dutyCycle between 0.0% and 100.0%

            GPIO.output(self.M1A, GPIO.LOW)
            GPIO.output(self.M1B, GPIO.HIGH)

            GPIO.output(self.M2A, GPIO.LOW)
            GPIO.output(self.M2B, GPIO.HIGH)

            # GPIO.PWM(pin, frequency)
            # frequency in Hz 
            p1 = GPIO.PWM(self.M1E, 100)
            p2 = GPIO.PWM(self.M2E, 100)
            
            p1.start(dutyCycle)
            p2.start(dutyCycle)

            # p.ChangeDutyCycle(90)
            # p.ChangeFrequency(100)

            sleep(duration)

            p1.stop()
            p2.stop()

            sleep(self.MOTOR_SETTLE_DUR)


    def backward(self, duration = 2, dutyCycle = 100):

            GPIO.output(self.M1A, GPIO.HIGH)
            GPIO.output(self.M1B, GPIO.LOW)

            GPIO.output(self.M2A, GPIO.HIGH)
            GPIO.output(self.M2B, GPIO.LOW)

            p1 = GPIO.PWM(self.M1E, 100)
            p2 = GPIO.PWM(self.M2E, 100)
            
            p1.start(dutyCycle)
            p2.start(dutyCycle)

            sleep(duration)

            p1.stop()
            p2.stop()

            sleep(self.MOTOR_SETTLE_DUR)


    def turnRight(self, duration = 3.8, dutyCycle = 100):

            GPIO.output(self.M1A, GPIO.HIGH)
            GPIO.output(self.M1B, GPIO.LOW)

            GPIO.output(self.M2A, GPIO.LOW)
            GPIO.output(self.M2B, GPIO.HIGH)

            p1 = GPIO.PWM(self.M1E, 100)
            p2 = GPIO.PWM(self.M2E, 100)
            
            p1.start(dutyCycle)
            p2.start(dutyCycle)

            sleep(duration)

            p1.stop()
            p2.stop()

            sleep(self.MOTOR_SETTLE_DUR)

    def turnLeft(self, duration = 3.8, dutyCycle = 100):

            GPIO.output(self.M1A, GPIO.LOW)
            GPIO.output(self.M1B, GPIO.HIGH)

            GPIO.output(self.M2A, GPIO.HIGH)
            GPIO.output(self.M2B, GPIO.LOW)

            p1 = GPIO.PWM(self.M1E, 100)
            p2 = GPIO.PWM(self.M2E, 100)
            
            p1.start(dutyCycle)
            p2.start(dutyCycle)

            sleep(duration)

            p1.stop()
            p2.stop()

            sleep(self.MOTOR_SETTLE_DUR)

    def stayHere(self, duration = 2):
        
            GPIO.output(self.M1A, GPIO.LOW)
            GPIO.output(self.M1B, GPIO.LOW)
            
            GPIO.output(self.M2A, GPIO.LOW)
            GPIO.output(self.M2B, GPIO.LOW)

            p1 = GPIO.PWM(self.M1E, 100)
            p2 = GPIO.PWM(self.M2E, 100)
            
            p1.start(0)
            p2.start(0)

            sleep(0.01)

            p1.stop()
            p2.stop()

            print "Staying here"
            sleep(duration)

            sleep(self.MOTOR_SETTLE_DUR)

    # --------- Sensors --------- 

    def getSensorsReady(self):

            GPIO.setmode(GPIO.BOARD)

            print "Getting sensors ready"
            GPIO.setup(self.S1T,GPIO.OUT)
            GPIO.setup(self.S1E,GPIO.IN)

            GPIO.setup(self.S2T,GPIO.OUT)
            GPIO.setup(self.S2E,GPIO.IN)

            GPIO.output(self.S1T, False)
            GPIO.output(self.S2T, False)

            sleep(self.SENSOR_SETTLE_DURATION)

    def pulseFront(self):

        GPIO.output(self.S1T, False)
        #print "Sensor settling"
        #sleep(0.03)

        GPIO.output(self.S1T, True)
        sleep(0.00001)        
        GPIO.output(self.S1T, False)

        while GPIO.input(self.S1E) == 0:
                pulse_start = time()

        while GPIO.input(self.S1E) == 1:
                pulse_end = time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        print "Front Distance", distance, "cm"

        return distance

    def pulseRight(self):

        GPIO.output(self.S2T, False)
        #print "Sensor settling"
        #sleep(0.03)

        GPIO.output(self.S2T, True)
        sleep(0.00001)        
        GPIO.output(self.S2T, False)

        while GPIO.input(self.S2E) == 0:
                pulse_start = time()

        while GPIO.input(self.S2E) == 1:
                pulse_end = time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        print "Right Distance", distance, "cm"

        return distance
        

    
