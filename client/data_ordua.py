import datetime
#print "The current local date time is ",datetime.datetime.now()

def data_ordua():
	dataordua = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	return dataordua