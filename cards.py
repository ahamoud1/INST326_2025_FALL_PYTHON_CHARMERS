import random

class Card:
    """Creates a playing card
    
    Attributes:
        rank (int): the number value of a card in a deck from
                    2-14, with 11=Jack, 12=Queen, 13=King, 14=Ace
        suit (str): the suit of the card in a deck 
                    (Hearts, Diamonds, Clubs, Spades)

    Done by:
        Ayah Hamouda
    """
    def __init__(self, rank, suit):
        """Initializes a card object
        
        Args:
            rank (int): the number value of a card in a deck,
                        see class documentation
            suit (str): the suit of the card in a deck,
                        see class documentation

        Side effects:
            Sets rank and suit attributes
        
        Techniques:
            Attributes

        Done by:
            Ayah Hamouda
        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """Informal, user friendly string representation of card 
        
        Returns:
            str: User friendly card

        Done by:
            Ayah Hamouda
        """
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
        """Formal, developer friendly string representation of card
        
        Returns:
            str: Developer friendly card

        Done by:
            Ayah Hamouda
        """
        return self.__str__()


def create_deck():
    """Creates a shuffled deck of cards
    
    Returns:
        randomized, shuffled list of card objects

    Done by:
        Ayah Hamouda
    """
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = list(range(2, 15))
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(rank, suit))
    random.shuffle(deck)
    return deck