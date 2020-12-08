playerAmount = int(input())
wallet = []
pot = 0
highBet = 0
currentBet = 0
playersFold = []

def default(playerAmount):
    lst = []
    for i in range(0,playerAmount):
        lst.append(100)

    return lst
    
def fold(player):
    global playersFold
    playersFold.append(player)
    
def call(player):
    global currentBet, pot, wallet

    if wallet[player] > currentBet:
        wallet[player] -= currentBet
        pot += currentBet
        return "call"
    if wallet[player] == currentBet:
        wallet[player] = 0
        pot += currentBet
        
        print("All in!")
        return "AllIn"
    
def bet(player, betAmount):
    global currentBet, pot, wallet

    if wallet[player] > betAmount + currentBet:
        wallet[player] -= betAmount
        highBet = i
        currentBet += betAmount
        pot += betAmount
        return "bet"
    elif wallet[player] == betAmount + currentBet:
        wallet[player] = 0
        currentBet += betAmount
        pot += betAmount
        print("All in!")
        return "AllIn"
    else:
        print("You don't have enough to do that")
        bet(i, int(input("How much do you bet? ")))

wallet = default(playerAmount)
while True:
    
    for i in range(0, playerAmount):

        if wallet[i] > 0 and not i in playersFold:
            print("It's player", i+1, "'s turn")
            print("Player", i+1, "has", wallet[i], "in his wallet")
            action = input("What do you want to do? f/c/b ")

            if action == "f" or action == "F":
                fold(i)
                
            elif action == "c":
                call(i)

            elif action == "b":
                bet(i, int(input("How much do you want to bet? ")))

            else:
                print("That is not a recognizeable action. You fold")
                fold(i)

    print("In the pot is now",pot,"$")
