import smtplib
import requests
import json

BASE_URL = "http://beer.zerbitzaria.ovh"

def get_pass():
	try:
		pas = open("pasahitza.txt").read().split("\n")[0]
		return pas
	except:
		return False


def mailez(tenperatura):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	pasahitza = get_pass()
	if not pasahitza:
		print "ERROREA!"
		print "sortu 'pasahitza.txt' artxiboa korreo elektronikoko pasahitzarekin."
		return False

	try:
		server.login("birrakomandoa@gmail.com", pasahitza)

		msg = str(tenperatura)
		server.sendmail("birrakomandoa@gmail.com", "birrakomandoa@gmail.com", msg)
		print "Tenperatura bidali da emailez..."
		server.quit()
	except Exception, e:
		print "Extepzioa tenperatura korreora bidaltzean "+str(e)
		print "Jarraitu egingo da..."

	return True


def datubasera(tenperatura):
	try:
		headers = {"Content-Type": "application/json"}
		json_data = {'tenp': tenperatura.tenp, 'garagardoa': tenperatura.garagardoa}
		r = requests.post(BASE_URL+"/ajax/add_temp", headers=headers, json=json_data)
		if r.status_code == 200:
			print "Tenperatura bidali da datu basera"
		else:
			print "Errorea tenperatura datu basera bidaltzean: "+r.reason
			print r.text[:200]
	except Exception, e:
		print "Extepzioa tenperatura datu basera bidaltzean "+str(e)
		print "Jarraitzen..."
