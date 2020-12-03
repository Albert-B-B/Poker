from random import randrange


def build_deck():
    numbers = range(2, 15)
    suits = ['H', 'S', 'C', 'D']
    deck = []
    for num in numbers:
        for suit in suits:
            card = suit + str(num)
            deck.append(card)
    return deck


def draw(deck, amount):
    drawn_cards = []

    for _ in range(amount):
        draw = randrange(1, len(deck))
        card = deck.pop(draw)
        drawn_cards.append(card)

    return drawn_cards


def is_straight_flush(hand, table):
    suits = ['H', 'S', 'C', 'D']
    hand_and_table = table + hand

    for suit in suits:
        for i in range(2, 6):
            for k in range(5):
                if suit + str(i + k) not in hand_and_table:
                    break
            else:
                return True
    return False


def is_straight(hand, table):
    hand_ranks = [int(card[1:]) for card in hand]
    table_ranks = [int(card[1:]) for card in table]

    hand_and_table = table_ranks + hand_ranks

    for i in range(2, 6):
        for k in range(5):
            if (i + k) not in hand_and_table:
                break
        else:
            return True
    return False


def is_flush(hand, table):
    suits = ['H', 'S', 'C', 'D']
    for suit in suits:
        count = 0
        for card in table:
            if suit in card:
                count += 1
        for card in hand:
            if suit in card:
                count += 1

        if count >= 5:
            return True
    return False


def is_of_a_kind(hand, table, amount):
    hand_ranks = [int(card[1:]) for card in hand]
    table_ranks = [int(card[1:]) for card in table]

    for i in range(2, 15):
        count = hand_ranks.count(i) + table_ranks.count(i)

        if count == amount:
            return True

    return False


def high_card(hand):
    hand_ranks = [int(card[1:]) for card in hand]
    return max(hand_ranks)


def is_two_pairs(hand, table):
    first_pair = False

    hand_ranks = [int(card[1:]) for card in hand]
    table_ranks = [int(card[1:]) for card in table]

    for i in range(2, 15):
        count = hand_ranks.count(i) + table_ranks.count(i)

        if count == 2 and not first_pair:
            first_pair = True
        elif count == 2:
            return True


def is_full_house(hand, table):
    pair = False
    three = False

    hand_ranks = [int(card[1:]) for card in hand]
    table_ranks = [int(card[1:]) for card in table]

    for i in range(2, 15):
        count = hand_ranks.count(i) + table_ranks.count(i)

        if count == 2:
            pair = True
        elif count == 3:
            three = True

    if pair and three:
        return True

    return False


OACf = 0
fullH = 0
fls = 0
strt = 0
OACth = 0
tOACt = 0
OACt = 0
hc = 0
sf = 0

#hand = ['D2','D3']
#table = ['D4','D5','D6','C4']

#print("Your hand is", hand)
#print("On the table is", table)

# straight flush
for i in range(0, 100):
    deck = build_deck()
    hand = draw(deck, 2)
    table = draw(deck, 5)

    if is_straight_flush(hand, table):
        print("You have a straight flush! Very cool!")
        sf += 1

    elif is_of_a_kind(hand, table, 4):
        print("You have four of a kind!")
        OACf += 1

    elif is_full_house(hand, table):
        print("You have full house")
        fullH += 1

    elif is_flush(hand, table):
        print("You have a flush")
        fls += 1

    elif is_straight(hand, table):
        print("You have a straight")
        strt += 1

    elif is_of_a_kind(hand, table, 3):
        print("You have three of a kind")
        OACth += 1

    elif is_two_pairs(hand, table):
        print("You have two pairs")
        tOACt += 1

    elif is_of_a_kind(hand, table, 2):
        print("You have a pair!")
        OACt += 1

    else:
        print("You have a high card with a value of", high_card(hand))
        hc += 1

print('Straight flushes:', sf, 'Four of a kind:', OACf, 'Full House:', fullH, 'flush:', fls, 'straight:',
      strt, 'three of a kind:', OACth, 'two pairs:', tOACt, 'pairs:', OACt, 'no hand/high card:', hc)
