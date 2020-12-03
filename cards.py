from __future__ import annotations
import enum


class Suit(enum.Enum):
    Hearts = enum.auto()
    Clubs = enum.auto()
    Diamonds = enum.auto()
    Spade = enum.auto()

    def __str__(self):
        return self.name


class Rank(enum.IntEnum):
    C2 = 2
    C3 = 3
    C4 = 4
    C5 = 5
    C6 = 6
    C7 = 7
    C8 = 8
    C9 = 9
    C10 = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    def __str__(self):
        return self.name.lstrip("C")


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card({repr(self.suit)}, {repr(self.rank)})"
    
    def __eq__(self, other: Card):
        return self.suit == other.suit and self.rank == other.rank


def build_deck():
    return [Card(suit, rank)
            for suit in Suit
            for rank in Rank]
