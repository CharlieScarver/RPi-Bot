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
	last = input;
	while input != "e":
                if input == "":
			options[last[0]](0.5, 100);
		else:
			options[input[0]](0.5, 100);
			last = input;
                input = raw_input();
                
	
except Exception as ex:
	clean();
	print "\nException: ",ex,"\n";
finally:
	clean();
	print "End";

