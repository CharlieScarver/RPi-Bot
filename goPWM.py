from InstructionsPWM import *

try:
        getReady()
        getSensorsReady()
        go()
        clean()
	
except Exception as ex:
	clean()
	print "\nException: ",ex,"\n"
finally:
	clean()
	print "End"

