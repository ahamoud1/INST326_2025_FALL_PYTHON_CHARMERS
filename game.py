"""runs game"""

from cards import create_deck
from initial_guess_phase import initial_guess_phase
from pyramid_matching import pyramid_round

def main():
    deck = create_deck()
    hand = initial_guess_phase(deck)
    matches = pyramid_round(deck,hand)

if __name__ == "__main__":
    main()