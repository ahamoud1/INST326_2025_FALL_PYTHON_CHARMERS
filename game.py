"""runs game"""

from cards import create_deck
from argparse import ArgumentParser
from initial_guess_phase import initial_guess_phase
from pyramid_matching import pyramid_round

def main():
    deck = create_deck()
    hand = initial_guess_phase(deck)
    matches = pyramid_round(deck,hand)
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("names", nargs="+", help="names of players")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    main()