from random import randrange, choices
import tkinter as tk

full_deck = ["Ace of spades", "2 of spades", "3 of spades", "4 of spades", "5 of spades", "6 of spades", "7 of spades", "8 of spades", "9 of spades", "10 of spades", "Jack of spades", "Queen of spades", "King of spades", "Ace of diamonds", "2 of diamonds", "3 of diamonds", "4 of diamonds", "5 of diamonds", "6 of diamonds", "7 of diamonds", "8 of diamonds", "9 of diamonds", "10 of diamonds", "Jack of diamonds", "Queen of diamonds",
             "King of diamonds", "Ace of hearts", "2 of hearts", "3 of hearts", "4 of hearts", "5 of hearts", "6 of hearts", "7 of hearts", "8 of hearts", "9 of hearts", "10 of hearts", "Jack of hearts", "Queen of hearts", "King of hearts", "Ace of clubs", "2 of clubs", "3 of clubs", "4 of clubs", "5 of clubs", "6 of clubs", "7 of clubs", "8 of clubs", "9 of clubs", "10 of clubs", "Jack of clubs", "Queen of clubs", "King of clubs"]
deck = full_deck.copy()

times_drawn = 0


def clicked():
    global times_drawn, cards

    times_drawn += 1
    if times_drawn == 1:
        cards = draw(3)
    elif times_drawn <= 3:
        cards.extend(draw(1))

    drawn_cards_label.configure(text=" | ".join(cards))


def draw(amount):
    drawn_cards = []

    for _ in range(amount):
        drawn = randrange(0, len(deck))
        card = deck.pop(drawn)
        drawn_cards.append(card)

    return drawn_cards


def bet():
    bet = 0
    try:
        bet = int(bet_input.get())
    except ValueError:
        bet_error.configure(text="Your bet must be a valid int")
    else:
        bet_error.configure(text="")

    return bet


def check():
    print(0)
    return 0


def call():
    print(0)
    return 0


def fold():
    print(0)
    return 0


i = 0

window = tk.Tk()
window.geometry('750x750')

window.title("Poker")

draw_button = tk.Button(window, text="Draw cards",
                        bg="orange", command=clicked)
draw_button.grid(column=0, row=i, sticky='W')
i += 1

drawn_cards_label = tk.Label(window, text="", font=("Arial Bold", 12))
drawn_cards_label.grid(column=0, row=i, columnspan=3, sticky='W')
i += 3

bet_input = tk.Entry(window, width=10)
bet_input.grid(column=0, row=i, sticky='W')
i += 1

bet_button = tk.Button(window, text="Bet", command=bet)
bet_button.grid(column=0, row=i, sticky='W')
bet_error = tk.Label(window, text="", fg="red")
bet_error.grid(column=1, row=i)
i += 2

check_button = tk.Button(window, text="Check", command=check)
check_button.grid(column=0, row=i, sticky='W')
i += 1
call_button = tk.Button(window, text="Call", command=call)
call_button.grid(column=0, row=i, sticky='W')
i += 1
fold_button = tk.Button(window, text="Fold", command=fold)
fold_button.grid(column=0, row=i, sticky='W')
i += 1

hand = draw(2)
hand_label = tk.Label(window, text=' and '.join(hand))
hand_label.grid(column=0, row=i, sticky='W')
window.mainloop()
