from initial_guess_phase import guesses

def ride_the_bus(deck, players):
    bus_player = max(players, key=lambda p: len(p.matches))
    print(f"\n{bus_player.name} is riding the bus")

    finished = False

    while not finished and len(deck) >= 4:
        print("\nNew attempt: ")
        cards, all_correct = guesses(deck)

        if all_correct:
            finished = True
        else:
            print("Restart!\n")

    print(f"{bus_player.name} finished Riding the Bus!")