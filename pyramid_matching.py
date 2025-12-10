def choice(prompt, valid=("y", "n"), default="n"):
    """ Prompts user for valid input
        
    Args:
        prompt(str): message shown by user
        valid (tuple): valid respones
        default (str): default value if user does not input
        
    Returns:
        str: valid user input

    Technique:
        Optional Parameters 

    Done by:
        Adela Wallis
    
    """
    
    while True:
        resp = input(prompt).strip().lower()
        if resp == "":
            return default
        if resp in valid:
            return resp
        print(f"Invalid input! Enter one: {valid}.")


def pyramid_round(deck, players):
    """Pyramid Round of the game

    Args:
        deck (list): deck of cards where rows are taken from
        players (list): list of player objects in round

    Side effects:
        updates player's hand and score
        records matches made by each player
        prints cards in each row and matched cards

    Technique:
        Sequence Unpacking

    Done by:
        Adela Wallis
    """

    for p in players:
        p.matches = []

    row_sizes = [5, 4, 3, 2, 1]
    row = 1

    for size in row_sizes:
        print(f"\n----- ROW {row}, {size} cards -----")

        row_cards = [deck.pop() for _ in range(size)]
        print("Flipped Cards:")
        for i, card in enumerate(row_cards, start=1):
            print(f" {i}. {card}")

        points = row  

        for p in players:
            matching_cards = [c for c in p.hand if any(c.rank == fc.rank for fc in row_cards)]
            
            if not matching_cards:
                print(f"\n{p.name} has no matching cards in the row")
                continue  
            
            print(f"\n{p.name} has matching card(s) in this row: {[str(c) for c in matching_cards]}")
            
            match = choice("do you want to match a card in this row? (y/n): ")

            
            while match == "y" and matching_cards:
                print("Which card do you want to use to match?")
                for i, c in enumerate(matching_cards, start=1):
                    print(f" {i}. {c}")
                selected = input(f"Enter number (1-{len(matching_cards)}): ").strip()
                
                try:
                    sel_index = int(selected) - 1
                    if not (0 <= sel_index < len(matching_cards)):
                        sel_index = 0
                except:
                    sel_index = 0

                selected_card = matching_cards.pop(sel_index)
                p.hand.remove(selected_card)
                p.matches.append((selected_card, row))
                p.add_score(points)
                
                print(f"{p.name} gained +{points} point(s)")
                

                if matching_cards:
                    match = choice(f"{p.name} do you want to match another card in this row? (y/n): ")
                else:
                    break  
        row += 1

    print("\n----- PYRAMID ROUND COMPLETE -----")

def print_pyramid_round(players):
    """Prints player summary of the pyramid round 
    
    Args:
        players (list): list of players

    Side effects:
        prints each player's matches and their current score

    Done by:
        Adela Wallis
    """

    print("\n----- PYRAMID ROUND SUMMARY -----")
    for p in players:
        print(f"\n{p.name}'s matches:")
        if not p.matches:
            print("  No matches")
        else:
            for card, row in p.matches:
                print(f"  Row {row}: {card}")
        print(f"Score: {p.score}")    

