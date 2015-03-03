from Instructions import *

try:
	getReady()

	forward(0.1)

	getSensorReady()
	pulse1()
	
except Exception as ex:
	clean()
	print "\nException: ",ex,"\n"
finally:
	clean()
	print "End"

