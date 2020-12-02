from random import randint

suits = ['H','S','C','D']

def build_deck():
    numbers = list(range(2, 15))
    global suits
    deck = []
    for i in numbers:
        for s in suits:
            card = s+str(i)
            deck.append(card)
    return deck

def draw(deck, amount):
    drawnCards = []
    
    for i in range(0, amount):
        length = len(deck) - 1
        draw = randint(1, length)
        drawnCards.append(deck[draw])
        del deck[draw]

    return drawnCards

def flush(hand, table):
    global suits
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

def fullHouse(hand, table):
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

deck = build_deck()
hand = draw(deck, 2)
table = draw(deck, 5)

hand = ['D11','C11']
table = ['H11','C2','H2','C5']

print("Your hand is", hand)
print("On the table is", table)


if flush(hand, table) == True:
    print("You have a flush")

elif fullHouse(hand, table) == True:
    print("You have full house")

elif OAC(hand, table, 4) == True:
    print("You have four of a kind!")

elif OAC(hand, table, 3) == True:
    print("You have three of a kind")

elif OAC(hand, table, 2) == True:
    print("You have a pair!")










    
