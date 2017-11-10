import os
import glob
import time
import smtplib
import RPi.GPIO as GPIO

import data_logging
import GPIO
import emailekoak

s = 0
piztuta = 0

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
    	datua = read_temp()
    	print(datua)
    	data_logging.data_logging(datua)
    	s=s+1
    	GPIO.ledgorriabehin()
    	if datua >= 10 and piztuta==0:
    		GPIO.konjeladoreapiztu()
    		piztuta=1
    	if datua < 9.6 and piztuta==1:
    		GPIO.konjeladoreaitzali()
    		piztuta=0

    	if s >= 30:
    		emailekoak.tenpemailez(datua)
    		s = 0

    	time.sleep(30)

if __name__ == "__main__":
    main()
