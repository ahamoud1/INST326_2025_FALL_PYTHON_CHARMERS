class Player:
    """
    Represents a player in the game.

    Attributes:
        name (str): The player's name.
        hand (list[Card]): The player's current hand of cards.
        matches (list[Card]): matched cards.
        score (int): The player's total score.

    Done by: Ranjith Mahendran 

    """
    def __init__(self, name):
        """
        Initialize a Player with a name and empty stats.

        Args:
            name (str): The player's name.
    
        Done by: Ranjith Mahendran 

        """
        self.name = name
        self.hand = []
        self.matches = []
        self.score = 0

    def set_hand(self, cards):
        """
        Deal a hand of cards to the player.

        Args:
            cards (list[Card]): The cards dealt to the player.

        Done by: Ranjith Mahendran 

        """
        self.hand = cards

    def add_score(self, points):
        """
        Add points to the player's total score.

        Args:
            points (int): The number of points to add.

        Done by: Ranjith Mahendran 

        """
        self.score += points
        
    def __str__(self):
        """
        Return the player's name as their string representation.

        Returns:
            str: The player's name.
       
        Done by: Ranjith Mahendran 

        """
        return self.name