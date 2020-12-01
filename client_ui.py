from random import randint
import tkinter as tk

fullDeck = ["Ace of spades","2 of spades","3 of spades","4 of spades","5 of spades","6 of spades","7 of spades","8 of spades","9 of spades","10 of spades","Jack of spades","Queen of spades","King of spades","Ace of diamonds","2 of diamonds","3 of diamonds","4 of diamonds","5 of diamonds","6 of diamonds","7 of diamonds","8 of diamonds","9 of diamonds","10 of diamonds","Jack of diamonds","Queen of diamonds","King of diamonds","Ace of hearts","2 of hearts","3 of hearts","4 of hearts","5 of hearts","6 of hearts","7 of hearts","8 of hearts","9 of hearts","10 of hearts","Jack of hearts","Queen of hearts","King of hearts","Ace of clubs","2 of clubs","3 of clubs","4 of clubs","5 of clubs","6 of clubs","7 of clubs","8 of clubs","9 of clubs","10 of clubs","Jack of clubs","Queen of clubs","King of clubs"]
deck = fullDeck.copy()

drawnCards = []
timesDrawn = 0

def clicked():

    global timesDrawn
    global cards
    timesDrawn += 1
    if timesDrawn == 1:
        cards = Draw(3)
    elif timesDrawn >= 4:
        lbl.configure(text=cards)
    else:
        cards.append(Draw(1))

    lbl.configure(text=cards)

def Draw(amount):

    global deck
    global drawnCards

    n = 0
    drawnCards = []
        
    while n < amount:
        length = int(len(deck)) -1
        drawn = randint(0,length)
        card = deck[drawn]
        del deck[drawn]
        n += 1
        drawnCards.append(card)

    return drawnCards

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

i = 0

window = tk.Tk()
window.geometry('750x750')

window.title("Poker")

btn = tk.Button(window, text="Draw cards", bg="orange", command=clicked)
btn.grid(column=0, row=i, sticky='W')
i += 1

lbl = tk.Label(window, text="", font=("Arial Bold", 12), )
lbl.grid(column=0, row=i, columnspan=3, sticky='W')
i += 3

txt = tk.Entry(window,width=10)
txt.grid(column=0, row=i, sticky='W')
i += 1

bet = tk.Button(window, text="Bet", command=Bet)
bet.grid(column=0, row=i, sticky='W')
betError = tk.Label(window, text="", fg = "red")
betError.grid(column=1, row=i)
i += 2

check = tk.Button(window, text="Check", command=Check)
check.grid(column=0, row=i, sticky='W')
i += 1
call = tk.Button(window, text="Call", command=Call)
call.grid(column=0,row=i, sticky='W')
i += 1
fold = tk.Button(window, text="Fold", command=Fold)
fold.grid(column=0,row=i, sticky='W')
i += 1

Hand = Draw(2)
YourCards = tk.Label(window, text=Hand)
YourCards.grid(column=0,row=i,sticky='W')
window.mainloop()
