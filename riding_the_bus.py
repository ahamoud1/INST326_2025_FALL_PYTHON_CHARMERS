import random

deck = (("Ace", "Diamonds"), ("Ace", "Clubs"), ("Ace", "Hearts"), ("Ace", "Spades"),
("2", "Diamonds"), ("2", "Clubs"), ("2", "Hearts"), ("2", "Spades"),
("3", "Diamonds"), ("3", "Clubs"), ("3", "Hearts"), ("3", "Spades"),
("4", "Diamonds"), ("4", "Clubs"), ("4", "Hearts"), ("4", "Spades"),
("5", "Diamonds"), ("5", "Clubs"), ("5", "Hearts"), ("5", "Spades"),
("6", "Diamonds"), ("6", "Clubs"), ("6", "Hearts"), ("6", "Spades"),
("7", "Diamonds"), ("7", "Clubs"), ("7", "Hearts"), ("7", "Spades"),
("8", "Diamonds"), ("8", "Clubs"), ("8", "Hearts"), ("8", "Spades"),
("9", "Diamonds"), ("9", "Clubs"), ("9", "Hearts"), ("9", "Spades"),
("10", "Diamonds"), ("10", "Clubs"), ("10", "Hearts"), ("10", "Spades"),
("Jack", "Diamonds"), ("Jack", "Clubs"), ("Jack", "Hearts"), ("Jack", "Spades"),
("Queen", "Diamonds"), ("Queen", "Clubs"), ("Queen", "Hearts"), ("Queen", "Spades"),
("King", "Diamonds"), ("King", "Clubs"), ("King", "Hearts"), ("King", "Spades"))

def ride_the_bus(players):
    """ The losing player will be determined and 10 cards will be laid face down and flipped one by one.
    Number cards do nothing while face cards and aces add penalty points to the losing player's score.

    Args:
        players (dict(str: int)): The names of the players and their scores
        cards (dict(str: str)): The different cards in regards to number and suit.

    Returns:
        player_points (int): The number of points that the losing player has after the Ride the Bus round.
        
    Side effects:
        prints the cards flipped by the losing player
    """
    losing_player = max(players, key=players.get)
    player_points = players[losing_player]

    for i in range(10):
        rank, suit = random.choice(deck)
        print(f"{losing_player} flipped {rank} of {suit}")

        if rank == "Ace":
            player_points += 4
        elif rank == "Jack":
            player_points += 1
        elif rank == "Queen":
            player_points += 2
        elif rank == "King":
            player_points += 3
        
    players[losing_player] = player_points
    return player_points

# Example Players
players = {
    "Player1": 22,
    "Player2": 18,
    "Player3": 31,
    "Player4": 14
}
new_score = ride_the_bus(players)
print(new_score)