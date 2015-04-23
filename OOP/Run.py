import PiBot

try:
	robot = PiBot('Dave')

	robot.getMotorsReady()
	robot.getSensorsReady()
	robot.go()
	
except Exception as ex:
	robot.clean()
	print(ex)

finally:
	robot.clean()
	print("End")

