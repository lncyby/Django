#!/usr/bin/python

from poplib import POP3
import getpass

p = POP3('pop.126.com')
p.user("lncyby@126.com")
pwd = getpass.getpass()

msg_ct,mbox_size = p.stat()
rsp,msg,siz = p.retr(msg_ct)

print rsp,siz

for echLine in msg:
    print eachLine
