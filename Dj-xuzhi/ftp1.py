#!/usr/bin/python

import ftplib
import os
import socket

HOST = 'ftp.kernel.org'
DIRN = 'put/linux/kernel'
FILE = 'README'

def main():

        f =  ftplib.FTP(HOST)

    f.quit()
    return

    print "*** Logged in as 'anongymous'"

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'Error:cannot CD to "%s"'%DORN
        f.quit()
        return

    print "*** Changed to 'folder'"%DIRN
