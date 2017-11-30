'''
Runs the wireless pidelity client.
Is currently a modified example of
socket programming from the python docs.
'''
import socket
import sys
import json

HOST = '192.168.12.1'     # The remote host
PORT = 50007              # The same port as used by the server
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
with s:

    sendme = json.JSONEncoder().encode({"type": "gpio", "op": "make", "pin": "27", "direction": "in"})
    print(sendme.encode('UTF-8'))
    s.sendall(sendme.encode('UTF-8'))