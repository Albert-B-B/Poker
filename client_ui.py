from random import randint
from tkinter import *
from PIL import Image, ImageTk

def build_deck():
    #builds the deck with cards, all following the format Suit - number. Ace is 14, king is 13 etc
    numbers = list(range(2, 15))
    suits = ['H','S','C','D']
    deck = []
    for i in numbers:
        for s in suits:
            card = s+str(i)
            deck.append(card)
    return deck

def draw(deck, amount):
    #returns an amount of random cards, and removes the cards chosen from the deck
    drawnCards = []
    
    for i in range(0, amount):
        length = len(deck) - 1
        draw = randint(1, length)
        drawnCards.append(deck[draw])
        del deck[draw]

    return drawnCards

def strflush(hand, table):
    #checks the hand and table for a straight flush
    suits = ['H','S','C','D']
    handTableSuit = table + hand
    
    count = 0
    for suit in suits:
        for i in range(0,6):
            if suit + str(i) in handTableSuit:
                count += 1
                if suit + str(i + 1) in handTableSuit:
                    count += 1
                    if suit + str(i + 2) in handTableSuit:
                        count += 1
                        if suit + str(i +3) in handTableSuit:
                            count += 1
                            if suit + str(i + 4) in handTableSuit:
                                count += 1
                                return True

def straight(hand, table):
    #checks hand and table for straights
    handCopy = hand.copy()
    tableCopy = table.copy()
    
    for i in range(0,2):
        handCopy[i] = handCopy[i][1:]
        handCopy[i] = int(handCopy[i])
    for i in range(0,4):
        tableCopy[i] = tableCopy[i][1:]
        tableCopy[i] = int(tableCopy[i])
    handTable = tableCopy + handCopy

    count = 0
    for i in range(0,6):
        if i in handTable:
            count += 1
            if i + 1 in handTable:
                count += 1
                if i + 2 in handTable:
                    count += 1
                    if i +3 in handTable:
                        count += 1
                        if i+4 in handTable:
                            count += 1
                            return True
    return False

def flush(hand, table):
    #checks hand and table for flushes
    suits = ['H','S','C','D']
    for i in suits:
        count = 0
        for string in table:
            if i in string:
                count += 1
        for string in hand:
            if i in string:
                count += 1

        if count >= 5:
            return True
    return False

def OAC(hand, table, amount):
    #checks hand and table for an amount of the same number-cards
    handCopy = hand.copy()
    tableCopy = table.copy()
    for i in range(0,2):
        handCopy[i] = handCopy[i][1:]
        handCopy[i] = int(handCopy[i])
    for i in range(0,4):
        tableCopy[i] = tableCopy[i][1:]
        tableCopy[i] = int(tableCopy[i])
    for i in range(2,15):
        count = handCopy.count(i) + tableCopy.count(i)
        
        if count == amount:
            return True
    return False

def highCard(hand):
    #determines and returns the highest card in the hand
    handCopy = hand.copy()
    for i in range(0,2):
        handCopy[i] = handCopy[i][1:]
        handCopy[i] = int(handCopy[i])
    a = max(handCopy)
    return a

def twopairs(hand, table):
    #checks hand and table for two pairs
    pair = False
    pair2 = False
    handCopy = hand.copy()
    tableCopy = table.copy()
    for i in range(0,2):
        handCopy[i] = handCopy[i][1:]
        handCopy[i] = int(handCopy[i])
    for i in range(0,4):
        tableCopy[i] = tableCopy[i][1:]
        tableCopy[i] = int(tableCopy[i])
    for i in range(2,15):
        count = handCopy.count(i) + tableCopy.count(i)
        
        if count == 2 and not pair:
            pair = True
        elif count == 2:
            pair2 = True

    if pair and pair2:
        return True


def fullHouse(hand, table):
    #checks hand and table for full house
    pair = False
    three = False
    handCopy = hand.copy()
    tableCopy = table.copy()
    for i in range(0,2):
        handCopy[i] = handCopy[i][1:]
        handCopy[i] = int(handCopy[i])
    for i in range(0,4):
        tableCopy[i] = tableCopy[i][1:]
        tableCopy[i] = int(tableCopy[i])
    for i in range(2,15):
        count = handCopy.count(i) + tableCopy.count(i)
        
        if count == 2:
            pair = True
        elif count == 3:
            three = True

    if pair and three:
        return True
    
    return False

windowX = 500
windowY = 500

drawnCards = []
timesDrawn = 0

def clicked():

    global t1, t2, t3, t4, t5, cards, timesDrawn, deck, table
    timesDrawn += 1
    if timesDrawn == 1:
        #river
        cards = [table[0], table[1], table[2]]
        t1.configure(image=table1)
        t2.configure(image=table2)
        t3.configure(image=table3)
        
    elif timesDrawn == 2:
        cards.append(table[timesDrawn + 1])
        t4.configure(image=table4)

    elif timesDrawn == 3:
        cards.append(table[timesDrawn + 1])
        t5.configure(image=table5)
        
        if strflush(hand, table) == True:
            handScore.configure(text="You have a straight flush! Very cool!")

        elif OAC(hand, table, 4) == True:
            handScore.configure(text="You have four of a kind!")

        elif fullHouse(hand, table) == True:
            handScore.configure(text="You have full house")

        elif flush(hand, table) == True:
            handScore.configure(text="You have a flush")

        elif straight(hand, table) == True:
            handScore.configure(text="You have a straight")

        elif OAC(hand, table, 3) == True:
            handScore.configure(text="You have three of a kind")

        elif twopairs(hand, table) == True:
            handScore.configure(text="You have two pairs")

        elif OAC(hand, table, 2) == True:
            handScore.configure(text="You have a pair!")

        else:
            highCardPrint = "You have a high card with a value of " + str(highCard(hand))
            handScore.configure(text=highCardPrint)

def Bet():
    Bet = 0
    try:
        Bet = int(txt.get())
        betError.configure(text="")
    except ValueError:
        betError.configure(text="Your bet must be a valid int")
    return  Bet

def Check():
    print(0)
    return 0

def Call():
    print(0)
    return 0

def Fold():
    print(0)
    return 0

def load(lst, nr):
    a = ImageTk.PhotoImage(Image.open("Assets/"+str(lst[nr-1])+".png"))
    return a

deck = build_deck()
hand = draw(deck, 2)
table = draw(deck, 5)

root = Tk()
root.geometry(str(windowX)+'x'+str(windowY))
root.title("Poker")

hand1 = load(hand, 1)
h1 = Label(root, image = hand1)
h1.place(x=140,y=335)

hand2 = load(hand, 2)
h2 = Label(root, image=hand2)
h2.place(x=200,y=335)

table1 = load(table, 1)
t1 = Label(root, image=None)
t1.place(x=20,y=150)

table2 = load(table, 2)
t2 = Label(root, image=None)
t2.place(x=120,y=150)

table3 = load(table, 3)
t3 = Label(root, image=None)
t3.place(x=220,y=150)

table4 = load(table, 4)
t4 = Label(root, image=None)
t4.place(x=320,y=150)

table5 = load(table, 5)
t5 = Label(root, image=None)
t5.place(x=420,y=150)

drw = Button(root, text="Draw cards", width=10, bg="orange", command=clicked)
drw.place(x=210, y=300)

txt = Entry(root,width=10)
txt.place(x=windowX/5*0+55,y=400)

bet = Button(root, text="Bet", command=Bet, width=10)
bet.place(x=windowX/5*0+55,y=425)
betError = Label(root, text="", fg = "red")
betError.place(x=1,y=375)

check = Button(root, text="Check", command=Check, width=10)
check.place(x=windowX/5*1+55,y=425)

call = Button(root, text="Call", command=Call, width=10)
call.place(x=windowX/5*2+55,y=425)

fold = Button(root, text="Fold", command=Fold, width=10)
fold.place(x=windowX/5*3+55,y=425)

handScore = Label(root, text="")
handScore.place(x=150,y=265)

root.mainloop()
