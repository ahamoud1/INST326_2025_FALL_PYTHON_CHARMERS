def choice(prompt, valid=("y", "n"), default="n"):
    while True:
        resp = input(prompt).strip().lower()
        if resp == "":
            return default
        if resp in valid:
            return resp
        print(f"Invalid input! Enter one: {valid}.")


def pyramid_round(deck, players):
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
``
        points = row  

        for p in players:
            matching_cards = [c for c in p.hand if any(c.rank == fc.rank for fc in row_cards)]
            
            if not matching_cards:
                print(f"\n{p.name} has no matching cards in the row")
                continue  
            
            print(f"\n{p.name} has matching card(s) in this row: {[str(c) for c in matching_cards]}")
            
            choice = input("do you want to match a card in this row? (y/n): ").strip().lower()
            while choice not in ["y", "n"]:
                choice = input("Invalid input! Enter 'y' to match or 'n' to skip: ").strip().lower()
            
            while choice == "y" and matching_cards:
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
                    choice = input(f"{p.name} do you want to match another card in this row? (y/n): ").strip().lower()
                    while choice not in ["y", "n"]:
                        choice = input("Invalid input! Enter 'y' to match or 'n' to skip: ").strip().lower()
                else:
                    break  
        row += 1

    print("\n----- PYRAMID ROUND COMPLETE -----")

def print_pyramid_round(players):
    print("\n----- PYRAMID ROUND SUMMARY -----")
    for p in players:
        print(f"\n{p.name}'s matches:")
        if not p.matches:
            print("  No matches")
        else:
            for card, row in p.matches:
                print(f"  Row {row}: {card}")
        print(f"Score: {p.score}")    

