#! /bin/python
from socket import *

# default params
serverAddr = ("", 50001)

import sys
def usage():
    print("usage: %s [--serverPort <port>]"  % sys.argv[0])
    sys.exit(1)

try:
    args = sys.argv[1:]
    while args:
        sw = args[0]; del args[0]
        if sw == "--serverPort":
            serverAddr = ("", int(args[0])); del args[0]
        else:
            print("unexpected parameter %s" % args[0])
            usage();
except:
    usage()

print("binding datagram socket to %s" % repr(serverAddr))

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(serverAddr)
print("ready to receive")

message, clientAddrPort = serverSocket.recvfrom(2048)
file = open(message,"wb+")

while True:
    #error handling
    try:
        message, clientAddrPort = serverSocket.recvfrom(2048)

    except:
        pass

    if not message:
        break
    #checking if end of file else writes to file
    if b"\'end\'" in message:
        file.close()
        sys.exit(0)
    else:
        file.write(message)
