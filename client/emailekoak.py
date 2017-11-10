import smtplib

def get_pass():
	return open("pasahitza.txt").read().split("\n")[0]

def tenpemailez(tenperatura):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
    pasahitza = get_pass()
	server.login("birrakomandoa@gmail.com", pasahitza)

	msg = str(tenperatura)
	server.sendmail("birrakomandoa@gmail.com", "birrakomandoa@gmail.com", msg)
	print "Tenperatura bidali da emailez........."
	server.quit()
