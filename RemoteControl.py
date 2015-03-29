from InstructionsPWM import *

try:
	getReady();

	options = {
                "w": forward,
                "s": backward,
                "d": turnRight,
                "a": turnLeft,
                "e": clean
        };

	input = raw_input();
	while input != "e":
                options[input[0]](0.5, 100);
                input = raw_input();
                
	
except Exception as ex:
	clean();
	print "\nException: ",ex,"\n";
finally:
	clean();
	print "End";

