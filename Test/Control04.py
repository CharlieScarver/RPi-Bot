from InstructionsPWM import *

try:
	getReady()

        forward(5, 100);
	
except Exception as ex:
	clean()
	print "\nException: ",ex,"\n"
finally:
	clean()
	print "End"

