"""runs game"""
import sys
from argparse import ArgumentParser
from cards import create_deck
from initial_guess_phase import guesses
from pyramid_matching import pyramid_round, print_pyramid_round
from players import Player
from riding_the_bus import ride_the_bus

def main():
    """
    Side effect: Executes the game flow for the Ride the Bus game. 

    Done by: Ranjith Mahendran

    """
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
    for p in players:
        print(f"\n{p.name}'s score: {p.score}")
        print(f"{p.name}'s hand: {p.hand}")   

    print(f"\n -----PYRAMID ROUND-----")
    
    pyramid_round(deck, players)
    print_pyramid_round(players)

    print(f"\n -----RIDING THE BUS-----")
    
    ride_the_bus_deck = create_deck()
    ride_the_bus(ride_the_bus_deck, players)
    
    print(f"\n-----FINAL SCORES-----\n")
    for p in players:
        print(f"{p.name}: {p.score}")
    
    winner = max(players, key=lambda p: p.score)
    print(f"\n{winner.name} wins with {winner.score} points!")

def parse_args(arglist):
    """
    Parse command line arguments for the game.

    Parameters:
    arglist : list[str]
        The list of arguments passed from the command line.

    Returns: 
    argparse
        An object containing parsed argument values, players: list of player names given by the user.
    
    Done by; Ranjith Mahendran
    """
    parser = ArgumentParser()
    parser.add_argument("players", nargs="+", help="players' names")
    return parser.parse_args(arglist)
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main()