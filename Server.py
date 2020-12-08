# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:11:29 2020

@author: albert.b.software@gamil.com
"""
# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading 
  
print_lock = threading.Lock() 
  
maxPlayers = 12
currentID = 0
defaultWallet = 15

users = []

class player:
    def __init__(self,ID,wallet,name):
        self.ID = ID
        self.wallet = wallet
        self.bet = 0
        self.name = name
        self.hand = []

# thread function 
def threaded(c): 
    global currentID
    global maxPlayers
    global users
    global defaultWallet
    # data received from client 
    data = c.recv(1024) 
    data = data.decode('ascii')
    
    #Pass
    if data[0:2] == "ID" and currentID < maxPlayers:
        print("User {} Joined".format(data[2:len(data)]))
        users.append(player(str(currentID),defaultWallet, (data[2:len(data)])))
        c.send(str(currentID).encode('ascii')) 
        currentID += 1
    #Return the current state of game including turn, river, layer hand, opponent bet and opponent fold. also shows showdown when relevant
    elif data == "STATE":
        pass
    #Sends number of players and their balance. Handles economy as opposed to state that handles hand info
    elif data == "GAMEINFO":
        pass
    #Recieves info on player action
    elif data == "BET":
        pass
    
    # connection closed 
    print_lock.release() 
    c.close() 
  
  
def Main(): 
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  

Main() 