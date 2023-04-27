#!/usr/local/bin/python
# Import smtplib for the actual sending function.
# Import argparse to be able to parse input parameters
import smtplib, argparse
#Just Handles basic text for the body of the message
from email.mime.text import MIMEText

parser = argparse.ArgumentParser(description='Send an email')
parser.add_argument('-g', help='gateway', dest='gw', required=True)
parser.add_argument('-f', help='from', dest='from_addr', required=True)
parser.add_argument('-t', help='to', dest='to_addr', required=True)
parser.add_argument('-s', help='subject', dest='subject', required=True)
parser.add_argument('-m', help='message text', dest='message_text', required=True)

args = parser.parse_args()
config = vars(args)

print ("Here's your configuration/request:")
print (config)

recipients = str(args.to_addr)
mysender = str(args.from_addr)

#setup the message
msg = MIMEText(str(args.message_text))
msg['Subject'] = str(args.subject)
msg['From'] = str(args.from_addr)
msg['To'] = recipients

print ("This will send to these recipients:")
print (recipients)

print (recipients.split(","))
#send the message
server = smtplib.SMTP(args.gw)
server.send_message(msg, mysender, recipients.split(","))
server.set_debuglevel(1)
server.quit()
