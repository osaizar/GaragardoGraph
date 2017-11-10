import smtplib

def tenpemailez(tenperatura):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
    pasahitza = open("pasahitza.txt").read().split("\n")[0]
	server.login("birrakomandoa@gmail.com", pasahitza)

	msg = str(tenperatura)
	server.sendmail("birrakomandoa@gmail.com", "birrakomandoa@gmail.com", msg)
	print "Tenperatura bidali da emailez........."
	server.quit()
