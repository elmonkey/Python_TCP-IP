# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 14:34:13 2014

TCP Server Example

ref: 
    https://docs.python.org/2/library/socketserver.html
    
NOTE:
    Try changin the list structures for sets - to speed up the process

@author: carlos
"""
import SocketServer

devs = []

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    
    Add devices to dev_list
    
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data  = self.request.recv(1024).strip().split(" ")
        self.devid = self.data[0]
        self.cmd   = self.data[1]
        self.msg   = ""

        dev = "dev{}".format(self.devid)
        
        # Add more dvices to dev_list
        dev_list = ['dev1', 'dev2', 'dev3']
        
#        print " ====== SERVER -- RUNNING ====== "
        print "{} wrote:".format(self.client_address[0])
        print "\t", self.data
        # Check device is on the list of allowed devices:
        if dev in dev_list:            
        
            # --- Connect the device "connect" command
            if self.cmd.lower() == "connect":
                print "\tAttempting to {} {}".format(self.cmd, dev)                                            
                if dev in devs:
                    self.msg = "dev{} -already connected".format(self.devid)
                else:
                    self.msg = "dev{}-ready".format(self.devid)
                    devs.append(dev)

            # --- Disconnect devices using  <dev1#> "disconnect"
            elif self.cmd.lower() == "disconnect":
                print "\tAttempting to {} {}".format(self.cmd, dev)                            
                if dev in devs:
                    devs.remove(dev)
                else:
                    self.msg = "dev{} -already disconnected".format(self.devid)
                    
            # --- Check status of connected devices using "check"
            elif self.cmd.lower() == "check":
                print "\tAttempting to {} {}".format(self.cmd, dev)
                if len(devs) ==0:
                    print '\t--No devices connected'
                    self.msg = 'not ready'
                # If all devices are accounted for... send 'Ready'
                elif len(devs) == len(dev_list):
                    print "\t--ALL devices are ready!"
                    self.msg = 'ready'
                else:# return the devid's of the currently connected devices
                    print "\t--List of connected devices: ",str(devs).strip('[]') 
                    self.msg = 'not ready' #str(devs).strip('[]')

            else: # unknown command
                print "Unknown command {}. Use connect, disconnect, or check".format(self.cmd)
            
        else: # dev not in list
            print "Unknown device {}. Please check devid try again!".format(dev)
            self.msg = "dev{} -Not recognised by the server!!".format(self.devid)
            
        # Check that ALL devices are ready

        print self.msg
        self.request.sendall(self.msg.lower())
        # print'Devices ready: ', devs

if __name__ == "__main__":
    #HOST, PORT = "localhost", 9999
    #HOST, PORT = "192.X.Y.Z", 9999
    #HOST = "192.X.Y.Z" # WiFi Net
    #HOST = "128.A.B.C" # Wired Net
    
    print " ====== SERVER -- RUNNING ====== "
    HOST = "localhost" # run locally
    PORT = 50007       # Arbitrary non-privileged port

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    
