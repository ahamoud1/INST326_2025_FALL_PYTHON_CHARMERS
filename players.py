class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.matches = []

    def set_hand(self, cards):
        self.hand = cards

    def __str__(self):
        return self.name