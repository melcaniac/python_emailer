#!/usr/local/bin/python
import smtplib, argparse
from email.mime.text import MIMEText

parser = argparse.ArgumentParser(description='Send an email')
parser.add_argument('-g', help='gateway', dest='gw', required=True)
parser.add_argument('-f', help='from', dest='from_addr', required=True)
parser.add_argument('-t', help='to', dest='to_addr', required=True)
parser.add_argument('-s', help='subject', dest='subject', required=True)
parser.add_argument('-d', help='message text', dest='text', required=True)

args = parser.parse_args()

#setup the message
msg = MIMEText(str(args.text))
msg['Subject'] = str(args.subject)
msg['From'] = str(args.from_addr)
msg['To'] = str(args.to_addr)

#send the message
s = smtplib.SMTP(args.gw)
s.sendmail(str(args.from_addr), [str(args.to_addr)], msg.as_string())
s.quit()
