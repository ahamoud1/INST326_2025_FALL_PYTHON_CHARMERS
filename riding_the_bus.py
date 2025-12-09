def ride_the_bus(deck, players):
    """ Player with lowest points is given 3 chances to choose between 10 cards.
    If the player gets a face card, they will gain points depending on the card given.
    """
    bus_player = min(players, key=lambda p: p.score)
    print(f"\n{bus_player.name} is riding the bus")

    cards = []
    for i in range(10):
        card = deck.pop()
        cards.append(card)
        
    values = {
        14: 4,
        13: 3,
        12: 2,
        1: 1
    }

    points = 0

    for pick in range(3):
        card_num = int(input("Pick a card (1-10): "))
        while card_num not in range(1, 11):
            card_num = int(input("Invalid! Pick a card (1-10): "))

        card_index = card_num - 1
        chosen_card = cards[card_index]
        print(f" {bus_player.name} has flipped {chosen_card}")
        print(f"You gained {values.get((chosen_card.rank), 0)} points!")

        points += values.get((chosen_card.rank), 0)

    bus_player.add_score(points)

    print(f"{bus_player.name} earned a total of {points} points!")