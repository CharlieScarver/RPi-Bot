import RPi.GPIO as GPIO
from time import *


class PiBot:

    name = 'PiBot'

    # Pins
    M1A = 16
    M1B = 18
    M1E = 22
    
    M2A = 23
    M2B = 21
    M2E = 19

    S1T = 11
    S1E = 13

    S2T = 7
    S2E = 15

    # Speed of Sound at sea level at 20 degrees celsius (in cm/s)
    SPEED_OF_SOUND = 34321

    # Max Motor Speed/PWM DutyCycle
    MAX_SPEED = 100

    # Settle and Move Durations (in seconds)
    MOTOR_SETTLE_DUR = 0.03
    MOVE_DUR_PER_TICK = 0.3

    INIT_SENSOR_SETTLE_DUR = 2.00
    SENSOR_SETTLE_DUR = 0.03
    SENSOR_PULSE_DUR = 0.00001 #(10 microseconds) 

    # Wall Detection Distances

    FRONT_WALL_DET_DIST = 15.0

    RIGHT_WALL_DET_DIST = 15.0


    # --------- Constructor ---------

    def __init__(self, newName):
        self.name = newName

    # --------- Main ---------

    def frontWallCheck(self):

        frontDist = self.pulseFront()
        
        if frontDist > self.FRONT_WALL_DET_DIST:
            return [False, frontDist]
        else:
            return [True, frontDist]

    def rightWallCheck(self):

        rightDist = self.pulseRight()
        
        if rightDist > self.RIGHT_WALL_DET_DIST:
            return [False, rightDist]
        else:
            return [True, rightDist]


    def go(self):

        lastDistsRight = [15.0, 15.0, 15.0, 15.0];

        while True:

            frontCheckResult = self.frontWallCheck()
            rightCheckResult = self.rightWallCheck()

            wallInFront = frontCheckResult[0]
            wallOnRight = rightCheckResult[0]

            lastDistsRight[2] = lastDistsRight[1]
            lastDistsRight[1] = lastDistsRight[0]
            lastDistsRight[0] = rightCheckResult[1]
                                                         
            while wallOnRight and not wallInFront:
                print("-----f-----")
                self.forward(self.MOVE_DUR_PER_TICK, self.MAX_SPEED)
                
                frontCheckResult = self.frontWallCheck()
                rightCheckResult = self.rightWallCheck()
                
                wallInFront = frontCheckResult[0]
                wallOnRight = rightCheckResult[0]

                lastDistsRight[2] = lastDistsRight[1]
                lastDistsRight[1] = lastDistsRight[0]
                lastDistsRight[0] = rightCheckResult[1]

                if lastDistsRight[0] > lastDistsRight[1] and lastDistsRight[1] > lastDistsRight[2] and lastDistsRight[2] > lastDistsRight[3]:
                    self.turnRight(0.1)

                if lastDistsRight[0] < lastDistsRight[1] and lastDistsRight[1] < lastDistsRight[2] and lastDistsRight[2] < lastDistsRight[3]:
                    self.turnLeft(0.1)          
                                    
                print("End of cycle")


    # --------- Cleanup ---------
    def clean(self):
            GPIO.cleanup()

    # --------- Basic Movement --------- 

    def getMotorsReady(self):
            
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

            sleep(self.INIT_SENSOR_SETTLE_DUR)

    def pulseFront(self):

        GPIO.output(self.S1T, False)
        #print "Sensor settling"
        sleep(self.SENSOR_SETTLE_DUR)

        GPIO.output(self.S1T, True)
        sleep(self.SENSOR_PULSE_DUR)       
        GPIO.output(self.S1T, False)

        while GPIO.input(self.S1E) == 0:
                pulse_start = time()

        while GPIO.input(self.S1E) == 1:
                pulse_end = time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * (self.SPEED_OF_SOUND / 2) #17150
        distance = round(distance, 2)

        print "Front Distance", distance, "cm"

        return distance

    def pulseRight(self):

        GPIO.output(self.S2T, False)
        #print "Sensor settling"
        sleep(self.SENSOR_SETTLE_DUR)

        GPIO.output(self.S2T, True)
        sleep(self.SENSOR_PULSE_DUR)
        GPIO.output(self.S2T, False)

        while GPIO.input(self.S2E) == 0:
                pulse_start = time()

        while GPIO.input(self.S2E) == 1:
                pulse_end = time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * (self.SPEED_OF_SOUND / 2) #17150
        distance = round(distance, 2)

        print "Right Distance", distance, "cm"

        return distance
        

    
