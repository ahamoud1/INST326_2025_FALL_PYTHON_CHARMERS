def guesses(deck):
    """
    Run the four initial guesses for a player.

    Args:
        deck (list[Card]): The deck to draw from. Four cards are removed.

    Side Effects:
        Prompts the user for input and prints results.

    Returns:
        tuple[list[Card], int]: The four drawn cards and the player's score.
    
    Done by: Ranjith Mahendran 
    """
    score = 0

    # Guess Color
    first = deck.pop()
    color_guess = input("Guess color (r/b): ").strip().lower()
    
    while color_guess not in ["r", "b"]:
        print("Invalid input! Enter 'r' for red or 'b' for black")
        color_guess = input("Guess color (r/b): ").strip().lower()
    actual_color = "r" if first.suit in ["Hearts", "Diamonds"] else "b"
    if color_guess == actual_color:
        print("Correct! You gained a point!\n")
        score += 1

    else:
        print("Wrong!\n")

    #Guess higher or lower
    second = deck.pop()
    hilo_guess = input("Higher or lower than first? (h/l): ").strip().lower()
    
    while hilo_guess not in ["h", "l"]:
        print("Invalid input! Enter 'h' for higher or 'l' for lower")
        hilo_guess = input("Higher or lower than first? (h/l): ").strip().lower()
    
    if (first.rank > second.rank and hilo_guess == "l") or \
       (first.rank < second.rank and hilo_guess == "h"):
        print("Correct! You gained a point!\n")
        score += 1

    else:
        print("Wrong!\n")

    #Guess inside or outside
    third = deck.pop()
    io_guess = input("Inside or outside the first two? (i/o): ").strip().lower()
    
    while io_guess not in ["i", "o"]:
        print("Invalid input! Enter 'i' for inside or 'o' for outside")
        io_guess = input("Inside or outside the first two? (i/o): ").strip().lower()
    
    low = min(first.rank, second.rank)
    high = max(first.rank, second.rank)
    inside = low < third.rank < high
    outside = third.rank < low or third.rank > high
    if (inside and io_guess == "i") or (outside and io_guess == "o"):
        print("Correct! You gained a point!\n")
        score += 1
    else:
        print("Wrong!\n")

    # Guess Suit
    fourth = deck.pop()
    suit_guess = input("Guess suit: (Hearts/Diamonds/Clubs/Spades): ").strip().lower()
    valid_suit = ["hearts", "diamonds", "clubs", "spades"]
    
    while suit_guess not in valid_suit:
        print("Invalid input! Enter Hearts, Diamonds, Clubs, or Spades")
        suit_guess = input("Guess suit: (Hearts/Diamonds/Clubs/Spades): ").strip().lower()
    if suit_guess == fourth.suit.lower():
        print("Correct! You gained a point!\n")
        score += 1
    else:
        print("Wrong!\n")

    return [first, second, third, fourth], score

