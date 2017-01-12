#!/usr/bin/python
#coding=utf-8

from ftplib import FTP
import sys,getpass,os.path

host,username,localfile,remotepath = sys.argv[1:]

password = getpass.getpass("Enter password for %s on %s:"%(username,host))

f = FTP(host)
f.login(username,password)
