from inst import *

try:
        getReady();
        getSensorsReady();
        go();
        clean();
	
except Exception as ex:
	clean()
	print(ex);
finally:
	clean()
	print("End");

