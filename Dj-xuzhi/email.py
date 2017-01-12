#!/usr/bin/python

import smtplib
from smtplib import SMTP as smtp
import getpass

mail_host = "smtp.126.com"
mail_user = "lncyby@126.com"
mail_pass = getpass.getpass()

sender = "lncyby@126.com"
receiver = ['lncyby@hotmail.com']

message = '''From:lncyby@126.com\r\nTo:lncyby@hotmail.com\r\nSubject:testmsg\r\n\r\nPython test email'''

print message

try:
    smtpobj = smtp(mail_host)
    smtpobj.login(mail_user,mail_pass)
    smtpobj.sendmail(sender,receiver,message)
    print "OK"

except smtplib.SMTPException,e:
    print "error:",e
