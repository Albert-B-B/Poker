from random import randrange, choices
import tkinter as tk

from cards import *

full_deck = build_deck()
deck = full_deck.copy()

times_drawn = 0


def clicked():
    global times_drawn, cards

    times_drawn += 1
    if times_drawn == 1:
        cards = draw(3)
    elif times_drawn <= 3:
        cards.extend(draw(1))

    drawn_cards_label.configure(text=" | ".join(map(str, cards)))


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
hand_label = tk.Label(window, text=' and '.join(map(str, hand)))
hand_label.grid(column=0, row=i, sticky='W')
window.mainloop()
