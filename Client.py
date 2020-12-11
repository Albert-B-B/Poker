# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:11:11 2020

@author: albert.b.software@gamil.com
"""
import socket 

ID = 0
ownWallet = 0
ownBet = 0 
turnBet = 0
canBet = False
name = input("What is your name?")
ownHand = []

winner = -1
otherPlayers = []
river = []

host = '127.0.0.1'
port = 12345

class player:
    def __init__(self,ID,wallet,name):
        self.ID = ID
        self.wallet = wallet
        self.bet = 0
        self.name = name
        self.hand = ["non","non"]
    def __repr__(self):
        return repr("ID: " + str(self.ID) + " wallet: " + str(self.wallet) + " bet: " + str(self.bet) + " name: " + str(self.name) + " Hand: " + str(self.hand[0])) + " " + str(self.hand[1])                               

def getState():
    global ID
    global host
    global port
    global canBet
    global turnBet
    global winner
    global otherPlayers
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
    # message you send to server 
    message = "STATE"
    # message sent to server 
    s.send(message.encode('ascii')) 
    # messaga received from server 
    data = s.recv(1024).decode('ascii').split('/')
    print(data)
    turnBet = int(data[1])
    #Checks if current turn is yours
    if turnBet == ID:
        canBet = True
        
    #Pre river case
    if int(data[0]) == 0:
        for i in range(2,len(data[2:len(data)]),2):
            for j in otherPlayers:
                if int(data[i]) == int(j.ID) and int(j.ID) != int(ID):
                    j.bet = int(data[i+1])
                    break
    #Showdown case
    elif int(data[0]) == 4:
        riverSize = int(data[0])+1
        for i in range(3,riverSize+3):
            river.append(data[i])
        for i in range(3+riverSize,len(data[2:len(data)]),4):
            for j in otherPlayers:
                if int(data[i]) == int(j.ID) and int(j.ID) != int(ID):
                    j.bet = int(data[i+1])
                    print(data[i+2])
                    j.hand = [data[i+2],data[i+3]]
                    break
    #Case if there is a river 
    else:
        riverSize = int(data[0])+2
        for i in range(2,riverSize+2):
            river.append(data[i])
        for i in range(2+riverSize,len(data[2:len(data)]),2):
            for j in otherPlayers:
                if int(data[i]) == int(j.ID) and int(j.ID) != int(ID):
                    j.bet = int(data[i+1])
                    break
    for i in otherPlayers:
        print(i)
    print(river)
    s.close() 
    
def getID(): 
    global name
    global host
    global port
    global otherPlayers
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
    print("Connected to server")
    # close the connection 
    
    s.close() 
    
def getGame():
    global otherPlayers
    host = '127.0.0.1'
  
    port = 12345
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    s.connect((host,port)) 
  

    message = "GAMEINFO"

    s.send(message.encode('ascii')) 
  

    data = s.recv(1024).decode('ascii')
    print(data)
    if '/' in data:
        data = data.split('/')
        for i in range(0,len(data),3):
            if data[i] != ID:
                otherPlayers.append(player(data[i],int(data[i+2]),data[i+1]))
    for i in otherPlayers:
        print(i)
    s.close() 
    
getID() 
getGame()
getState()