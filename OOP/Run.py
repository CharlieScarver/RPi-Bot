from PiBot import PiBot

robot = PiBot('Dave')

try:
	robot.setGPIOMode()
	robot.getMotorsReady()
	robot.getSensorsReady()
	robot.go()
	
except Exception as ex:
	robot.clean()
	print(ex)

finally:
	robot.clean()
	print("End")

