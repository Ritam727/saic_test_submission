# Task 2
I wrote the script in python and used subprocess, os, sys and smtplib modules in order to complete this task. This script takes as command line arguments the email of the user, a flag showing whether the argument would be a domain or an ip address and then scans the ip address(es) for open ports, the services on those ports and their versions. The script also gives details of the geographic location of the ip address(es).

I created a file `ip_info.py` and wrote the following code in the file:
```python
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
```

What the code does is it looks up for the ip address(es) of the domain if the ip address is not provided and then scans for the geographic location of the ip address(es) using an API named **ipinfo**. It then scans for the open ports in the ip address(es). Once finished it saves the details in .txt format and then sends the file as an attachment over mail to the user.

Usage:
1. For scanning a domain name:

    `$ sudo python ip_info.py [email_of_user] -d [domain]`

    Replace [email_of_user] with your email-id and [domain] with the domain you want to scan. For eg, if you want to scan `www.example.com` and your email-id is `name@domain.com`, then issue the following command:

    `$ sudo python ip_info.py name@domain.com -d www.example.com`
2. For scanning ip addresses

    `$ sudo python ip_info.py [email_of_user] -i [ip1] [ip2] [ip3] ...`
    
    Replace [email_of_user] with your email-id and [ip1], [ip2], [ip3], ... with ip addresses you want to scan. For eg, if you want to scan `111.222.333.1`, `111.222.333.2`, `111.222.333.3` and `111.222.333.4`, and your email-id is `name@domain.com`, then issue the following command:

    `$ sudo python ip_info.py name@domain.com -i 111.222.333.1 111.222.333.2 111.222.333.3 111.222.333.4`

---
---

# What I learnt
Use of nslookup to find ip address of a domain and use of nmap to scan an ip address and use of ipinfo API to get location details of an ip address. Also, the use of smtplib to send mails and attachments.

# Difficulties faced
I faced a lot of difficulties in configuring the smtp for sending the attachment over mail. I had to do a lot of googling while completing this part of the task. At one time the mail was sent with the attachment, but the attachment became encoded and was unreadable directly. Later on, I found the problem was in the encoding part. So, I looked up for different methods and found one in GeeksforGeeks and was able to send the proper mail.

# Resources used
1. A lot of google
2. GeeksforGeeks
