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
maxNameLength = 10
currentID = 0
defaultWallet = 15

users = []
winner = -1

maxBet = 10
turnBet = 0
turnRiver = 0
smallBlind = 5
bigBlind = 10
currentMaxBet = 1
river = []
class player:
    def __init__(self,ID,wallet,name):
        self.ID = ID
        self.wallet = wallet
        self.bet = 0
        self.name = name
        self.hand = ["non","non"]

# thread function 
def threaded(c): 
    global currentID
    global maxPlayers
    global users
    global defaultWallet
    global turnBet
    global turnRiver
    global winner
    global maxNameLength
    global maxBet
    # data received from client 
    data = c.recv(1024) 
    data = data.decode('ascii')
    
    #Pass
    if data[0:2] == "ID" and currentID < maxPlayers:
        if maxNameLength < len(data) - 2:
            c.send("Our name is too long".encode('ascii'))
        else:
            print("User {} Joined".format(data[2:len(data)]))
            users.append(player(str(currentID), defaultWallet, (data[2:len(data)])))
            c.send(str(currentID).encode('ascii')) 
            currentID += 1
    #Return the current state of game including turn, river, layer hand, opponent bet and opponent fold. also shows showdown when relevant
    elif data == "STATE":
        message = ""
        message += str(turnRiver) + '/'
        message += str(turnBet) + '/'
        #Normal turn
        if turnRiver != 4:
            if turnRiver > 0:
                for i in river:
                    message += i + '/'
            for i in users:
                message += str(i.ID) + '/' + str(i.bet) + '/'
            message = message[:len(message)-1]
            c.send(message.encode('ascii'))
        #Showdown
        else:
            message += str(winner) + '/'
            if turnRiver > 0:
                for i in river:
                    message += i + '/'
            for i in users:
                message += str(i.ID) + '/' + str(i.bet) + '/' + str(i.hand[0]) + '/' + str(i.hand[1]) + '/'
            message = message[:len(message)-1]
            c.send(message.encode('ascii'))
            
    #Sends number of players and their balance. Handles economy as opposed to state that handles hand info
    elif data == "GAMEINFO":
        message = ""
        for i in users:
            message += str(i.ID) + '/' + str(i.name) + '/' + str(i.wallet) + '/'
        if len(message) > 1:
            message = message[:len(message)-1]
        c.send(message.encode('ascii'))
    #Recieves info on player action
    elif data[0:3] == "BET":
        data = data.split('/')
        if int(data[1]) == turnBet:
            #Just check
            if int(data[2]) == 0 and users[data[1]].wallet + users[data[1]].bet - currentMaxBet > 0:
                users[data[1]].wallet = users[data[1]].wallet + users[data[1]].bet - currentMaxBet
                users[data[1]].bet = currentMaxBet
                #Implement all in
                if users[data[1]].wallet == 0:
                    pass
            #User made bet
            elif users[data[1]].wallet + users[data[1]].bet - int(data[2]) > 0 and users[data[1]].bet - int(data[2]) < maxBet and int(data[2]) > 0:
                users[data[1]].wallet = users[data[1]].wallet + users[data[1]].bet - int(data[2])
                users[data[1]].bet = int(data[2])
            #User is all in
            elif users[data[1]].wallet - int(data[2]) == 0 or int(data[2]) == 0:
                pass
            #Player folds
            elif int(data[2]) == -1:
                users[data[1]].bet = int(data[2])
            else:
                c.send("Too large bet. Not enough money in wallet".encode('ascii'))
            turnBet = (turnBet + 1) % len(users)
    elif data[0:4] == "HAND":
        data = data.split('/')
        a = int(data[1])
        message = str(users[a].hand[0]) + '/' + str(users[a].hand[1])
        c.send(message.encode('ascii'))
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