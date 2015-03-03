from InstructionsPWM import *

try:
	getReady()
        forward(2)
	#turnRight(2)
        backward(2,30)
	clean()
	
except Exception as ex:
	clean()
	print "\nException: ",ex,"\n"
finally:
	clean()
	print "End"

