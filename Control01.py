from Instructions import *

try:
	getReady()

	forward(1)
	turnRight(2)
	forward(0.5)
	turnLeft(2)
	backward(2)
except:
	clean()
	print "\nException"
finally:
	clean()
	print "End"

