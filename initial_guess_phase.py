
def initial_guess_phase(deck):
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
    return [first, second, third, fourth]

