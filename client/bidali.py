import smtplib
import requests
import json

BASE_URL = "http://localhost:5000"

def get_pass():
	return open("pasahitza.txt").read().split("\n")[0]

def mailez(tenperatura):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	pasahitza = get_pass()
	server.login("birrakomandoa@gmail.com", pasahitza)

	msg = str(tenperatura)
	server.sendmail("birrakomandoa@gmail.com", "birrakomandoa@gmail.com", msg)
	print "Tenperatura bidali da emailez........."
	server.quit()

def datubasera(tenperatura):
	headers = {"Content-Type": "application/json"}
	json_data = {'tenp': tenperatura.tenp, 'garagardoa': tenperatura.garagardoa}
	r = requests.post(BASE_URL+"/ajax/add_temp", headers=headers, json=json_data)
	if r.status_code == 200:
		print "Tenperatura bidali da datu basera"
	else:
		print "Errorea tenperatura bidaltzean: "+r.reason
		print r.text[:200]
