import RPi.GPIO as GPIO
import time
import smtplib
import data_logging

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

def ledgorriabehin():
	GPIO.output(17,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(17,GPIO.LOW)

def konjeladoreapiztu():
	print "relea:---------------------------PIZTU"
	GPIO.output(22,GPIO.HIGH)
	data_logging.konjeladorea_logging(1)

def konjeladoreaitzali():
	print "relea:-------ITZALI"
	GPIO.output(22,GPIO.LOW)
	data_logging.konjeladorea_logging(0)
