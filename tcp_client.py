# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 14:40:55 2014

tcp_client.py

ref: 
    https://docs.python.org/2/library/socketserver.html
    
Example usage:
    python tcp_client dev<id> <cmmd>

OR:
    ids = [1,2,3]
    cmmds   = ['check', 'connect', 'disconnect']
    #To connect device 1
    dev = 'dev'+str(ids[0])
    cmmd = cmmds[1]
    
    python tcp_client dev cmmd -> dev1 connected # on server

@author: carlos
"""

import socket
import sys

#HOST, PORT = "localhost", 9999
#HOST, PORT = "192.X.Y.Z", 9999
# OR 
#HOST = "192.X.Y.Z"  # WiFi Net
#HOST = "128.A.B.C"  # Wired Net
#HOST = "localhost"  # local server/client

HOST = "localhost"   # Server IP address
PORT = 50007         # The same port as used by the server

#data = " ".join(sys.argv[1:])
if len(sys.argv) <2:
    print "Usage: python tcp_client.py <devid> <message>"
    sys.exit()
devid=     sys.argv[1] #"testing"
data =     sys.argv[2]

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(devid + " " + data + "\n")

    # Receive data from the server and shut down
    received = sock.recv(1024)
    
    print "Command sent: {}".format(data)
    print "Server reply: {}".format(received)
    
finally:
    sock.close()
