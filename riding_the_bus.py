from initial_guess_phase import play_guess_round

def ride_the_bus_phase(deck, players):
    bus_player = max(players, key=lambda p: len(p.matches))
    print(f"\n{bus_player.name} is riding the bus")

    finished = False

    while not finished and len(deck) >= 4:
        print("\nNew attempt: ")
        cards, all_correct = play_guess_round(deck)

        if all_correct:
            finished = True
        else:
            print("Restart!\n")

    print(f"{bus_player.name} finished Riding the Bus!")