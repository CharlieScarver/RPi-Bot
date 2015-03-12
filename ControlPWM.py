from InstructionsPWM import *
from time import *

try:
	getReady()
        getSensorsReady()

        #forward(2, 100)
	#turnLeft(3.8, 100)
	#backward(2, 100)
        #turnRight(2, 100)
	#print "I'm here"

        #while True:
        #    while pulseRight() < 15.0:
        #        forward(0.3)
        #    while pulseFront() < 15.0:
        #        backward(0.3)
        
	
except Exception as ex:
	clean()
	print "\nException: ",ex,"\n"
finally:
	clean()
	print "End"

