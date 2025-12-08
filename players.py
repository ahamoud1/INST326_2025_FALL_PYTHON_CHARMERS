class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.matches = []
        self.score = 0

    def set_hand(self, cards):
        self.hand = cards

    def add_score(self, points):
        self.score += points
        
    def __str__(self):
        return self.name