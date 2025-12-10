import random
def bus_player(players):
    """ Randomly determines the player who will ride the bus if at least two players have the lowest score.
    If else, then it will return the player with the lowest score.
    
    Args:
        players (list[Player]): The player objects and their scores.
        
    Returns:
        player(Player): The player object with the lowest score.
    
    Side effects:
        Prints message if there are more than two losing players.
    """
    lowest_score = min(player.score for player in players)
    lowest_players = [player for player in players if player.score == lowest_score]
    if len(lowest_players) > 1:
        print("There is a tie for the lowest score. A random player will be chosen to ride the bus")
        return random.choice(lowest_players)
    else:
        return lowest_players[0]
        
def ride_the_bus(deck, players):
    """ Player with lowest points is given 3 chances to choose between 10 cards.
    If the player gets a face card, they will gain points depending on the card given.
    
    Args:
        deck(list[Card]): The card deck that will be used in the final round.
        players (list[Player]): The player objects and their scores.
        
    Side effects:
        Modifies deck by removing cards for round.
        Requires input from the user to flip cards
        Prints messages to inform the player
        Modifies player's score.
    """
    
    bus_rider = bus_player(players)
    print(f"\n{bus_rider.name} is riding the bus")

    cards = []
    for i in range(10):
        card = deck.pop()
        cards.append(card)
        
    values = {
        14: 4,
        13: 3,
        12: 2,
        11: 1
    }

    points = 0

    for pick in range(3):
        card_num = int(input("Pick a card (1-10): "))
        while card_num not in range(1, 11):
            card_num = int(input("Invalid! Pick a card (1-10): "))

        card_index = card_num - 1
        chosen_card = cards[card_index]
        print(f" {bus_rider.name} has flipped {chosen_card}")
        print(f"You gained {values.get((chosen_card.rank), 0)} points!")

        points += values.get((chosen_card.rank), 0)

    bus_rider.add_score(points)

    print(f"{bus_rider.name} earned a total of {points} points!")