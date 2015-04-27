from PiBot import PiBot

robot = PiBot("Dave")

try:
	robot.setGPIOMode()
	robot.getMotorsReady()

	input = raw_input();
	last = input;
	while input != "e":
		if input == "":
			input  = last;
			continue
		else:
			last = input;
			if input == "w":
				robot.forward(0.5)
			elif input == "s":
				robot.backward(0.5)
			elif input == "d":
				robot.turnRight(0.2)
			elif input == "a":
				robot.turnLeft(0.2)			

                input = raw_input();

	robot.clean()
                
	
except Exception as ex:
	robot.clean()
	print("\nException: ",ex,"\n")
finally:
	robot.clean()
	print("End")

