from InstructionsPWMIdeal import *

try:
	getReady()
	getSensorsReady()
	go()
	
except Exception as ex:
	clean()
	print(ex)

finally:
	clean()
	print("End")

