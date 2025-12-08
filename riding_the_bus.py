import random

def ride_the_bus(deck, players):
    bus_player = min(players, key=players.score)
    print(f"\n{bus_player.name} is riding the bus")

    card_choices = []
    
    for i in range(10):
        card_choices += random.choice(deck)
        
    for k in range(3):
        card_num = input("Pick a card (1-10)").strip()
        while (card_num+1) < 0 or (card_num+1) > 10:
            print("Invalid input! Enter a number between 1 and 10")
            card_num = input("Pick a card (1-10)").strip()
        if card_choices.rank(card_num) == "Ace":
            player_points += 4
        elif card_choices.rank(card_num) == "King":
            player_points += 3
        elif card_choices.rank(card_num) == "Queen":
            player_points += 2
        elif card_choices.rank(card_num) == "Jack":
            player_points +=1
        else:
            player_points += 0
    print (f"\n{bus_player.name} finished Riding the Bus!")
    return player_points