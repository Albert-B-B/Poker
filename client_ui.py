from random import randint
from tkinter import *
from PIL import Image, ImageTk

scores = []
results = []

windowX = 500
windowY = 500

drawnCards = []
timesDrawn = 0

playerAmount = int(input("How many players? "))

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
    handCopy = hand.copy()
    tableCopy = table.copy()

    total = handCopy + tableCopy
    iTotal = []
    for i in range(0,2):
        handCopy[i] = handCopy[i][1:]
        handCopy[i] = int(handCopy[i])
    for i in range(0,4):
        tableCopy[i] = tableCopy[i][1:]
        tableCopy[i] = int(tableCopy[i])
    for i in range(2,15):
        a = total.count(i)
        
        if a == 2:
            iTotal.append(a)

    if len(iTotal) >= 2:
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

def check_winner(hands, table):
    scores = []
    a = len(hands)
    
    for i in range(0, a):
        hand = hands[i]
        
        if strflush(hand, table) == True:
            scores.append(22)

        elif OAC(hand, table, 4) == True:
            scores.append(21)

        elif fullHouse(hand, table) == True:
            scores.append(20)
        
        elif flush(hand, table) == True:
            scores.append(19)

        elif straight(hand, table) == True:
            scores.append(18)

        elif OAC(hand, table, 3) == True:
            scores.append(17)

        elif twopairs(hand, table) == True:
            scores.append(16)

        elif OAC(hand, table, 2) == True:
            scores.append(15)

        else:
            scores.append(highCard(hand))

    m = 0
    winners = []
    players = []
    delete = []
    
    for i in range(0, len(scores)):
        players.append(i)
        if scores[i] >= max(scores):
            winners.append(i)

    for i in range(0, len(scores)):
        if scores[i] < max(scores):
            scores[i] = 0

    n = 0
    for i in range(0, len(scores)):
        if scores[n] == 0:
            del scores[n]
            del players[n]
        else:
            n += 1
        
    return players

def clicked():

    global t1, t2, t3, t4, t5, cards, timesDrawn, deck, table, hands
    timesDrawn += 1
    if timesDrawn == 1:
        #river
        cards = [table[0], table[1], table[2]]
        t1.configure(image=table1)
        t1.place(x=20,y=150)
        t2.configure(image=table2)
        t2.place(x=120,y=150)
        t3.configure(image=table3)
        t3.place(x=220,y=150)
        
    elif timesDrawn == 2:
        cards.append(table[timesDrawn + 1])
        t4.configure(image=table4)
        t4.place(x=320,y=150)

    elif timesDrawn == 3:
        cards.append(table[timesDrawn + 1])
        t5.configure(image=table5)
        t5.place(x=420,y=150)
        
        w = check_winner(hands, table)
        print("Winner is player number", w)

def hands(playerAmount):
    global deck
    a = []
    for i in range(0,playerAmount):
        b = draw(deck, 2)
        a.append(b)
    return a

def Bet():
    Bet = 0
    try:
        Bet = int(txt.get())
        betError.configure(betError.place_forget())
        
    except ValueError:
        betError.configure(text="Your bet must be a valid int")
        betError.place(x=1,y=375)
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
hands = hands(playerAmount)
table = draw(deck, 5)
print(hands)

root = Tk()
root.geometry(str(windowX)+'x'+str(windowY))
root.title("Poker")

background_image = ImageTk.PhotoImage(Image.open("Assets/backdrop.png"))
background_label = Label(root, image=background_image)
background_label.place(x=-2, y=-2)

hand1 = load(hands[0], 1)
h1 = Label(root, image = hand1)
h1.place(x=140,y=335)

hand2 = load(hands[0], 2)
h2 = Label(root, image=hand2)
h2.place(x=200,y=335)

if playerAmount >= 2:
    backImg = ImageTk.PhotoImage(Image.open("Assets/back.png"))
    ch1 = Label(root, image= backImg)
    ch1.place(x=55,y=30)

    ch2 = Label(root, image= backImg)
    ch2.place(x=75,y=30)

if playerAmount >= 3:
    ch3 = Label(root, image= backImg)
    ch3.place(x=155,y=30)

    ch4 = Label(root, image= backImg)
    ch4.place(x=175,y=30)

if playerAmount >= 4:
    ch5 = Label(root, image= backImg)
    ch5.place(x=255,y=30)

    ch6 = Label(root, image= backImg)
    ch6.place(x=275,y=30)

if playerAmount >= 5:
    ch7 = Label(root, image= backImg)
    ch7.place(x=355,y=30)

    ch7 = Label(root, image= backImg)
    ch7.place(x=375,y=30)

table1 = load(table, 1)
t1 = Label(root, image=None)

table2 = load(table, 2)
t2 = Label(root, image=None)

table3 = load(table, 3)
t3 = Label(root, image=None)

table4 = load(table, 4)
t4 = Label(root, image=None)

table5 = load(table, 5)
t5 = Label(root, image=None)

drw = Button(root, text="Draw cards", width=10, bg="orange", command=clicked)
drw.place(x=210, y=300)

txt = Entry(root,width=10)
txt.place(x=windowX/5*0+55,y=400)

bet = Button(root, text="Bet", command=Bet, width=10)
bet.place(x=windowX/5*0+55,y=425)
betError = Label(root, text="", fg = "red")

check = Button(root, text="Check", command=Check, width=10)
check.place(x=windowX/5*1+55,y=425)

call = Button(root, text="Call", command=Call, width=10)
call.place(x=windowX/5*2+55,y=425)

fold = Button(root, text="Fold", command=Fold, width=10)
fold.place(x=windowX/5*3+55,y=425)

handScore = Label(root, text="")

root.mainloop()
