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
    actual_color = "r" if first.suite in ["Hearts", "Diamonds"] else "b"
    print("You were", "right!" if color_guess == actual_color else "wrong.")
    #score points

    #Guess higher or lower
    second = deck.pop()
    hilo_guess = input("Higher or lower than first? (h/l): ")
    if (first.rank > second.rank and hilo_guess == "l") or \
       (first.rank < second.rank and hilo_guess == "h"):
        print("Correct!")
        #score points
    else:
        print("Wrong!")

    #Guess inside or outside
    third = deck.pop()
    io_guess = input("Inside or outside the first two? (i/o): ")
    low = min(first.rank, second.rank)
    high = max(first.rank, second.rank)
    inside = low < third.rank < high
    outside = third.rank < low or third.rank > high
    if (inside and io_guess == "i") or (outside and io_guess == "o"):
        print("Correct!")
        #score points
    else:
        print("Wrong!")

    #Guess suit
    fourth = deck.pop()
    suit_guess = input("Guess suit (h/d/c/s): ")
    if suit_guess == fourth.suite:
        print("Correct!")
        #score points
    else:
        print("Wrong!")

    print("Your cards were:", first, second, third, fourth)
    return [first, second, third, fourth]

