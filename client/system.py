import os
import glob
import time

import data_logging
import GPIO
import bidali
from models import Tenperatura

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


s = 0
goran = 1
hasera = 1
estufa = 0

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c


def main():
    # Init
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    # Main loop


while True:
    tenp = Tenperatura(read_temp())
    print (str(tenp))

    if s==60:
    	data_logging.data_logging(tenp.tenp)

    if tenp.tenp >= 20 and (goran == 0 or hasera==1):
    	GPIO.konjeladoreapiztu()
    	GPIO.estufaitzali()
        goran=1
    	hasera=0
    	estufa=0

    if tenp.tenp < 20 and (goran == 1 or hasera==1):
    	GPIO.konjeladoreaitzali()
    	#GPIO.estufapiztu()
    	estufa=1
        goran=0
    	hasera=0

    if estufa == 1:
    	GPIO.estufapiztu()
    	time.sleep(4)
    	GPIO.estufaitzali()
    	time.sleep(4)


    if s==60:
    	#bidali.mailez(tenp.tenp)
        bidali.datubasera(tenp)
    	s = 0

    s=s+1
    time.sleep(1)

if __name__ == "__main__":
    main()
