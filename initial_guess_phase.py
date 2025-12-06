def play_guess_round(deck):
    all_correct = True

    first = deck.pop()
    color_guess = input("Guess color (r or b): ")
    actual_color = "r" if first.suit in ["Hearts", "Diamonds"] else "b"
    if color_guess == actual_color:
        print("Correct!\n")
    else:
        print("Wrong!\n")
        all_correct = False

    second = deck.pop()
    hilo_guess = input("Higher or lower than first? (h/l): ")
    if (first.rank > second.rank and hilo_guess == "l") or \
       (first.rank < second.rank and hilo_guess == "h"):
        print("Correct!\n")
    else:
        print("Wrong!\n")
        all_correct = False

    third = deck.pop()
    io_guess = input("Inside or outside the first two? (i/o): ")
    low = min(first.rank, second.rank)
    high = max(first.rank, second.rank)
    inside = low < third.rank < high
    outside = third.rank < low or third.rank > high
    if (inside and io_guess == "i") or (outside and io_guess == "o"):
        print("Correct!\n")
    else:
        print("Wrong!\n")
        all_correct = False

    fourth = deck.pop()
    suit_guess = input("Guess suit: (Hearts/Diamonds/Clubs/Spades): ")
    if suit_guess == fourth.suit:
        print("Correct!\n")
    else:
        print("Wrong!\n")
        all_correct = False

    return [first, second, third, fourth], all_correct

