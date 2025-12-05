"""runs game"""

from cards import create_deck
from initial_guess_phase import initial_guess_phase
from pyramid_matching import pyramid_round
from players import Player

def main():
    deck = create_deck()

    num_players = int(input("Enter number of players: "))
    players = []

    for i in range(num_players):
        name = input("Enter name for player " + str(i + 1) + ": ")
        player = Player(name)
        players.append(player)

    for player in players:
        print("\nPlayer:", player.name)
        hand = initial_guess_phase(deck)
        player.set_hand(hand)
        matches = pyramid_round(deck, player.hand)
        player.set_matches(matches)

    print("\nGame over. Summary:")
    for player in players:
        print(f"\nPlayer: {player.name}")
        print(f"Hand: {player.hand}")
        print(f"Matches: {player.matches}")

if __name__ == "__main__":
    main()