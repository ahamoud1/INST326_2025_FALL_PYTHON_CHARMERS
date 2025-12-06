"""Creates a card object and a deck of random cards!"""

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.rank == 11:
            rank_name = "Jack"
        elif self.rank == 12:
            rank_name = "Queen"
        elif self.rank == 13:
            rank_name = "King"
        elif self.rank == 14:
            rank_name = "Ace"
        else:
            rank_name = str(self.rank)
        return rank_name + " of " + self.suit
    
    def __repr__(self):
        return self.__str__()


def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = list(range(2, 15))
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(rank, suit))
    random.shuffle(deck)
    return deck