#!/usr/bin/python

import os
import signal
import socket
from SocketServer import BaseRequestHandler,ThreadingTCPServer
import threading
import subprocess
from multiprocessing import Process

class Handler(BaseRequestHandler):
    def handle(self):
        address,pid = self.client_address
        while True:
            data = self.request.recv(1024)
            if len(data)>0:
                printdata = data + ":" + address + "\n"
                print ('The %s ip: %s' % (data,address))
                filename = "../Connected_machine.txt"
                if os.path.exists(filename):
                    mode = "a"
                else:
                    mode = "w"
                with open(filename,mode) as f:
                    f.write(printdata)
            else:
                break

if __name__ == '__main__':
    host = ''
    port = 9999
    addr = (host,port)
    server = ThreadingTCPServer(addr,Handler)
    print 'listening'
    server.serve_forever()
