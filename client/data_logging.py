import os
from datetime

def data_ordua():
	return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def data_logging(tenp):
	s = str(tenp)
	file = open("/home/pi/LogFiles/data_log.txt", "a")

	file.write(data_ordua())

	file.write("  --  ")
	file.write(s)
	file.write("\n")

	file.close()

def konjeladorea_logging(x):
	if x == 1:
		r = "relea:------------------------------------PIZTU"
	else:
		r = "relea:-----------ITZALI"

	file = open("/home/pi/LogFiles/data_log.txt", "a")

	file.write("\n")
	file.write(r)
	file.write("\n")
	file.write("\n")

	file.close()
