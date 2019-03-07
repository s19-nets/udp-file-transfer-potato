#! /bin/python
from socket import *
import os

# default params
serverAddr = ('localhost', 50000)

import sys, re

def usage():
    print("usage: %s [--serverAddr host:port]"  % sys.argv[0])
    sys.exit(1)

try:
    args = sys.argv[1:]
    while args:
        sw = args[0]; del args[0]
        if sw == "--serverAddr":
            addr, port = re.split(":", args[0]); del args[0]
            serverAddr = (addr, int(port))
        else:
            print("unexpected parameter %s" % args[0])
            usage();
except:
    usage()

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(0.8)
#ack = false
#message = input("Input lowercase msg:")
#clientSocket.sendto(message.encode(), serverAddr)
#modifiedMessage, serverAddrPort = clientSocket.recvfrom(2048)
#print("Modified message from %s is <%s>" % (repr(serverAddrPort), modifiedMessage))
files = os.listdir(os.curdir)
print(files)
inputFile =input("Enter name of file: ")
try:
    with open(inputFile.strip(),"rb") as binary_file:
        data = binary_file.read()
except FileNotFoundError:
    print("file not found, Exiting")
    sys.exit(0)

while len(data) >= 100:
    line = data[:100]
    data = data[100:]
    clientSocket.sendto(data, serverAddr)
    if len(data) > 0:
        clientSocket.sendto(data, serverAddr)
        clientSocket.sendto(b":\'end\'", serverAddr)

#while not ack:
#    try:
#        ACK, address = clientSocket.recvfrom(2048)
#        future=time.time()+0.8
#        ack = True
#    except timeout:
#        clientSocket.sendto(data, serverAddr)
#print(ACK)
