"""runs game"""

from cards import create_deck
from initial_guess_phase import initial_guess_phase

def main():
    deck = create_deck()
    initial_guess_phase(deck)

if __name__ == "__main__":
    main()