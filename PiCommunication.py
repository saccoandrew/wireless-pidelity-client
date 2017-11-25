'''
Make process automated for setting up connection, create library for use as input
Created on Oct 30, 2017

@author: saccoa1
'''
'''
import json
import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit();
 
print 'Socket Created'

host = 'www.google.com'#host to be changed to connect to pi
port = 80
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
     
print ('Ip address of ' + host + ' is ' + remote_ip)
 
#Connect to remote server
s.connect((remote_ip , port))
 
print ('Socket Connected to ' + host + ' on ip ' + remote_ip)
 
#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
 
try :
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
 
print 'Message send successfully'
'''

#from nt import lstat
#import requests
#import socket
#from test.test_json.test_pass1 import JSON
def wipi(data):

#Opening Socket
#sock = socket.socket()
#sock.connect((address, port))

#importing JSON
#jsonData = {"name": "Frank", "age": 39}
#jsonToPython = json.loads(jsonData)

#python to JSON

#pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
#dictionaryToJson = json.dumps(pythonDictionary)

    i=input("Enter number of variables: ")
    type(i)

    lst=[0]#contain collection of values
    n=10 #to be resized for number of params needed
    for i in range(1, n):
        lst.append(i)

    print (lst)

    #lst
    #lst.append('a')
    #for a in lst:

    wipi.addParam("speed")
    wipi.setParam(speed,10)
    wipi.sendJson()   

def getVars():
    x=input("Enter number of variables: ")
    type(x)
    return x

def main():
    num_vars=getVars #number of vars that will be taken in
    index=0
    datatype=[0]*num_vars
    var_total=0 #accumulate number of variables created
    
    while index<num_vars:
        print("for data ", index+1, ": ")
        datatype[index]=int(input())
        index += 1