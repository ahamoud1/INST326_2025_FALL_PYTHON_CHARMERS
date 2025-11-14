""" 
    Adela Wallis' Function - check_for_matches
    
    writing a func that checks player's hand to see if they have
    cards that match the cards in pyramid
    
"""

def player_hand():
    """player's hand of cards
    """
    
    hand = {
        "6": ("red", "hearts"), 
        "3": ("red", "diamonds"), 
        "Ace": ("black", "spades"),
        "2": ("red", "hearts")}
    
    return hand

def pyramid_formation():
    """the cards that are in the pyramid
    """
    
    pyramid = [
        [{"4": ("black", "clubs")}, {"3": ("red", "clubs")}, {"Queen": ("red", "hearts")}, {"7": ("black", "spades")}, {"9": ("red", "hearts")}],
        [{"2": ("red", "hearts")}, {"King": ("black", "spades")}, {"10": ("red", "diamonds")},{"5": ("black", "clubs")}],
        [{"Ace": ("black", "spades")}, {"6": ("red", "hearts")}, {"8": ("black", "clubs")}],
        [{"Jack": ("red", "diamonds")}, {"4": ("black", "clubs")}],
        [{"3": ("red", "hearts")}]]
    
    return pyramid

def check_for_matches(player_hand):

    pyramid = pyramid_formation()

    for row in pyramid:
        for card in row:
            rank, (color, suit) = list(card.items())[0]
            print(f"Flipped Card -> {rank}: {color}, {suit}")
            
            if rank in player_hand:
                player_color, player_suit = player_hand[rank]
                print("\nTheres a match!\n")
                print(f"Your card -> {rank}: {player_color},{player_suit}")
                print(f"Card in Pyramid -> {rank}: {color}, {suit}")
                return (rank, color, suit)
            
            
    print("No cards match")
    return None
            
hand = player_hand()
check_for_matches(hand)  
