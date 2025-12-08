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

    print(f"\n ----- INITIAL GUESS PHASE -----")
    
    for name in args.players:
        p = Player(name)
        print("\nPlayer:", p.name)
        hand, score = guesses(deck)
        p.set_hand(hand)
        p.add_score(score)
        players.append(p)
        print(f"{p.name}'s score: {p.score}")
        
    print(f"\n -----PYRAMID ROUND-----")
    
    pyramid_round(deck, players)
        
    for p in players:
        print(f"\nPlayer: {p.name}")
        print(f"Hand: {p.hand}")
        print(f"Matches: {[str(card) for card, r in p.matches]}")
        
        for r in range(1,5):
            row_matches = [card for card, rr in p.matches if rr==r]
            if row_matches:
                print(f"Row {r} matches: {[str(c) for c in row_matches]} "
                      f"{len(row_matches) * r} points")
                
        print(f"Score: {p.score}")
        
    print(f"\n -----RIDING THE BUS-----")
    
    ride_the_bus(deck,players)
    
    print(f"\n-----FINAL SCORES-----\n")
    for p in players:
        print(f"{p.name}: {p.score}")

if __name__ == "__main__":
    main()