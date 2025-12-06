"""runs game"""
import argparse
from cards import create_deck
from initial_guess_phase import guesses
from pyramid_matching import pyramid_round
from players import Player
from riding_the_bus import ride_the_bus

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("players", nargs="+", help="players' names")
    args = parser.parse_args()
   
    deck = create_deck()
    players = []

    for name in args.players:
        p = Player(name)
        print("\nPlayer:", p.name)
        hand, all_correct = guesses(deck)
        p.set_hand(hand)
        players.append(p)
        
    pyramid_round(deck, players)
    
    print("\nSummary:")
    for p in players:
        print(f"\nPlayer: {p.name}")
        print(f"Hand: {p.hand}")
        print(f"Matches: {p.matches}")
        
    ride_the_bus(deck,players)

if __name__ == "__main__":
    main()