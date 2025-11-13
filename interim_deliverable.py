"""Project Interim Deliverable
    Ayah Hamouda
    INST326
    November 13, 2025
"""

import random 

def random_select():
    """Randomly selects four cards from a standard 52 card deck.

    Returns:
        list: four randomly selected cards from the deck.
        
    Side effects:
        - prints a list of four cards to the output console.
    """
    standard_deck = ["2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS",
                     "KS", "AS",
                     "2H","3H","4H","5H","6H","7H","8S","9H","10H","JH","QH",
                     "KH", "AH",
                     "2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC",
                     "KC","AC",
                     "2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD",
                     "KD","AD"]
    
    four_cards = []
    
    while len(four_cards) < 4:
        card = random.choice(standard_deck)
        if card not in four_cards:
            four_cards.append(card)
    
    print(four_cards)
    return four_cards

random_select()

