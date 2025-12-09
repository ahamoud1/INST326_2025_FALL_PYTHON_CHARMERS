"""runs game"""
import sys
from argparse import ArgumentParser
from cards import create_deck
from initial_guess_phase import guesses
<<<<<<< HEAD
from pyramid_matching import pyramid_round, print_pyramid_round
=======
from pyramid_matching import pyramid_round as pyramid_round
>>>>>>> f8fcf592154db331b539ac3427e3d81527df491a
from players import Player
from riding_the_bus import ride_the_bus

def main(players):   
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

        print(f"\n ----- INITIAL GUESS PHASE RESULT -----")

        print(f"{p.name}'s score: {p.score}")
        print(f"{p.name}'s hand: {p.hand}")

    print(f"\n -----PYRAMID ROUND-----")
    
    pyramid_round(deck, players)
<<<<<<< HEAD
    print_pyramid_round(players)
=======
>>>>>>> f8fcf592154db331b539ac3427e3d81527df491a

    print(f"\n -----RIDING THE BUS-----")
    
    ride_the_bus_deck = create_deck()
    ride_the_bus(ride_the_bus_deck, players)
    
    print(f"\n-----FINAL SCORES-----\n")
    for p in players:
        print(f"{p.name}: {p.score}")
    
    winner = max(players, key=lambda p: p.score)
    print(f"\n{winner.name} wins with {winner.score} points!")

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("players", nargs="+", help="players' names")
    return parser.parse_args(arglist)
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.players)