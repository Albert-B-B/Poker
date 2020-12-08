# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:11:11 2020

@author: albert.b.software@gamil.com
"""
import socket 

ID = 0

def getID(): 
    
    name = input("What is your name?")
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Define the port on which you want to connect 
    port = 12345
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
    # message you send to server 
    message = "ID" + name
    # message sent to server 
    s.send(message.encode('ascii')) 
  
    # messaga received from server 
    data = s.recv(1024) 
  
    # print the received message 
    # here it would be a reverse of sent message 
    print('Received from the server :',str(data.decode('ascii'))) 
    # close the connection 
    s.close() 
getID() 