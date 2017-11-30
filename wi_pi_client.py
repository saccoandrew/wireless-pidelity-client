'''
Runs the wireless pidelity client.
Is currently a modified example of
socket programming from the python docs.
'''
import socket
import sys

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print ("Could not open socket")
    sys.exit(1)
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print ("Received", repr(data))