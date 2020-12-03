from random import randint

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

#variables for each of the 9 hands. Not necessary for normal play.
OACf = 0
fullH = 0
fls = 0
strt = 0
OACth = 0
tOACt = 0
OACt = 0
hc = 0
sf = 0

#iterates i times. For normal play, keep at range at (0,1).
for i in range(0,1):
    #builds deck and deals
    deck = build_deck()
    hand = draw(deck, 2)
    table = draw(deck, 5)

    print("Your hand is", hand)
    print("On the table is", table)
    
    #sets a predetermined hand. Only used for testing
    #hand = ['D2','D3']
    #table = ['D4','D5','D6','C4']
    if strflush(hand, table) == True:
        print("You have a straight flush! Very cool!")
        sf += 1
    
    elif OAC(hand, table, 4) == True:
        print("You have four of a kind!")
        OACf += 1

    elif fullHouse(hand, table) == True:
        print("You have full house")
        fullH += 1

    elif flush(hand, table) == True:
        print("You have a flush")
        fls += 1

    elif straight(hand, table) == True:
        print("You have a straight")
        strt += 1

    elif OAC(hand, table, 3) == True:
        print("You have three of a kind")
        OACth += 1

    elif twopairs(hand, table) == True:
        print("You have two pairs")
        tOACt += 1

    elif OAC(hand, table, 2) == True:
        print("You have a pair!")
        OACt += 1

    else:
        print("You have a high card with a value of", highCard(hand))
        hc += 1
#Prints amount of each hand pulled in i simulations. Not necessary for normal play
'''
print('In {} simulations you got '.format(i))
print('Straight flushes:', sf)
print('Four of a kind:',OACf)
print('Full House:', fullH)
print('Flush:',fls)
print('Straight:', strt)
print('Three of a kind:', OACth)
print('Two pairs:', tOACt)
print('Pairs:', OACt)
print('No hand/High card:',hc)
'''
