import os
import time 
from time import sleep
from datetime import datetime

import data_ordua

def data_logging(tenp):
	s = str(tenp)
	file = open("/home/pi/LogFiles/data_log.txt", "a")

	file.write(data_ordua.data_ordua())
	
	file.write("  --  ")
	file.write(s)
	file.write("\n")

def konjeladorea_logging(x):
	if x==0:
		file = open("/home/pi/LogFiles/data_log.txt", "a")

		file.write("\n")
		file.write("relea:-----------ITZALI")
		file.write("\n")
		file.write("\n")

	if x==1:
		file = open("/home/pi/LogFiles/data_log.txt", "a")

		file.write("\n")
		file.write("relea:------------------------------------PIZTU")
		file.write("\n")
		file.write("\n")




	
