#!/usr/bin/python

import socket

HOST = '128.224.153.74'
PORT = 9999
ADDR = (HOST,PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(ADDR)
    data = socket.gethostname()
    s.send(data)
    print "connect"
except socket.error as msg:
    print "Socket Error: %s" % msg

s.close()
