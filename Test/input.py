from Instructions import *
import time
import RPi.GPIO as GPIO

def eventHandler (pin):
	print "stop"
	stop()

def main():
	GPIO.setmode(GPIO.BOARD)

#GIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)*/

	Trig = 11
	Echo = 13

#	GPIO.setup(Echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	GPIO.add_event_detect(Echo, GPIO.RISING)
#	GPIO.add_event_callback(Echo, eventHandler, 100)

#        ultrasonicPulse()
#	forward(3)

        distance = ultrasonicPulse()
        while not(GPIO.event_detected(Echo)) or distance > 15.0:
                forward(0.3)
                distance = ultrasonicPulse()
                

getReady()
getSensorReady()
main()
clean()
	
