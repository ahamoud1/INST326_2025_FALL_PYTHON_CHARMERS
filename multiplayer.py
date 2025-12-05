import random
import sys
from argparse import ArgumentParser

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


def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = list(range(2, 15))
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(rank, suit))
    random.shuffle(deck)
    return deck

class Player:
    """ A Player, the cards on hand.
    
    Attributes:
        name (str): The player's name.
        cards (list): The player's cards.
        points (int): The points the player has acquired.
    """
    
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0
    
    """def user_deck(self, deck):
        for i in range(4):
            self.cards.append(deck.pop())"""
              
    def initial_guess_phase(self, deck):
        """Play the initial guess phase of the Ride the Bus game using a given deck.
        
        Args:
            deck (list):a shuffled deck of card objects.
        
        Side Effects:
            plays the initial round and updates scores.
        
        Returns:
            cards (card) drawn card objects
        """

        #Guess color
        first = deck.pop()
        color_guess = input("Guess color (r or b): ")
        actual_color = "r" if first.suit in ["Hearts", "Diamonds"] else "b"
        print("Correct!\n" if color_guess == actual_color else "Wrong!\n")
        #score points

        #Guess higher or lower
        second = deck.pop()
        hilo_guess = input("Higher or lower than first? (h/l): ")
        if (first.rank > second.rank and hilo_guess == "l") or \
        (first.rank < second.rank and hilo_guess == "h"):
            print("Correct!\n")
            #score points
        else:
            print("Wrong!\n")

        #Guess inside or outside
        third = deck.pop()
        io_guess = input("Inside or outside the first two? (i/o): ")
        low = min(first.rank, second.rank)
        high = max(first.rank, second.rank)
        inside = low < third.rank < high
        outside = third.rank < low or third.rank > high
        if (inside and io_guess == "i") or (outside and io_guess == "o"):
            print("Correct!\n")
            #score points
        else:
            print("Wrong!\n")

        #Guess suit
        fourth = deck.pop()
        suit_guess = input("Guess suit (Hearts/Diamonds/Clubs/Spades): ")
        if suit_guess == fourth.suit:
            print("Correct!\n")
            #score points
        else:
            print("Wrong!\n")

        print(f"Your cards were:\n{first}\n{second}\n{third}\n{fourth}\n")
        self.cards = [first, second, third, fourth]
        return self.cards

class Pyramid():
    def __init__(self):
        self.matches = []
    def pyramid_round(self, deck, hand):
        self.matches = []

        for i in range(10):
            card = deck.pop()
            for h in hand:
                if h.rank == card.rank:
                    self.matches.append(card)
                    break

        print(f"Number of matches in pyramid round: {len(self.matches)}")
        return self.matches
        
def main(names):
    deck = create_deck()
    players = []
    winner = []
    losing_player = []
    
    for name in names:
        players.append(Player(name))
        
    # Initial Guess Phase
    print("Round 1")
    for player in players:
        print(f"{player.name}'s Turn")
        player.initial_guess_phase(deck)
        
    # Pyramid Phase
    pyramid = Pyramid()   
    print("Round 2")
    for player in players:
        print(f"{player.name}'s Turn")
        matches = pyramid.pyramid_round(deck, player.cards)
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("names", nargs="+", help="names of players")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.names)