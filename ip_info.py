import subprocess as sb
import os, sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def main():
	f = open("details.txt", "w")
	if os.getuid() != 0:
		print("Please run as root!!")
		os.system("rm -f details.txt")
		exit(1)
	args = sys.argv[2:]
	ips = []
	if args[0] == "-d":
		outs = sb.run("sudo nslookup "+args[1]+" | grep 'Address: '", shell = True, capture_output = True).stdout.decode("utf-8")
		outs = outs.split("\n")
		for out in outs:
			ips.append(out[9:])
		ips.pop()
	elif args[0] == "-i":
		ips = args[1:]
	else:
		print("No flag found for ip or domain!! Invalid syntax!!")
		os.system("rm -f details.txt")
		exit(1)
	if args[0] == "-d":
		msg = "ip addresses associated with the domain are:"
		f.write(msg+"\n")
		for ip in ips:
			f.write(ip+"\n")
		f.write("\n")
	for ip in ips:
		d = eval(sb.run("curl https://ipinfo.io/"+ip, shell = True, capture_output = True).stdout.decode("utf-8"))
		if 'status' in d.keys() and d['status'] == 404:
			print("Invalid ip")
			os.system("rm -f details.txt")
			exit(1)
		f.write("Geographical location of the ip address "+ip+" is:\n")
		f.write(d['region']+", "+d['country']+"\n")
		f.write(d['loc']+"\n\n")
		ports = sb.run("sudo nmap -Pn -sV "+ip+" | grep open", shell = True, capture_output = True).stdout.decode("utf-8")
		f.write("List of open ports on the ip address "+ip+" and their services and versions:\n")
		f.write(ports+"\n\n\n")
	f.close()
	f = open("details.txt", "r")
	print(f.read())

	fromaddr = "b20127@students.iitmandi.ac.in"
	toaddr = sys.argv[1]
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Info on IP"
	body = "PFA the details of the ip address you decided to inspect."
	msg.attach(MIMEText(body, 'plain'))
	filename = "details.txt"
	attachment = open(filename, "rb")
	p = MIMEBase('application', 'octet-stream')
	p.set_payload((attachment).read())
	encoders.encode_base64(p)
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(p)
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(fromaddr, "Rtm@1234#")
	text = msg.as_string()
	s.sendmail(fromaddr, toaddr, text)
	s.quit()
	os.system("rm -f details.txt")

main()
