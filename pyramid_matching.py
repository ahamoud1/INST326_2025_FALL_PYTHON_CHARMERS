def pyramid_round(deck, players):
    for p in players:
        p.matches = []
        
    row_sizes = [4, 3, 2, 1]
    row = 1

    for size in row_sizes:
        points = len(row_sizes) - (row - 1)
        for i in range(size):   
            card = deck.pop()
            for p in players:
                for h in p.hand:
                    if h.rank == card.rank:
                        p.matches.append((card, row))
                        p.add_score(points)
                        break  
        row += 1

def print_pyramid_round(players):  
    for p in players:
        print(f"\nPlayer: {p.name}") 

        print("Matches:", [str(c) for c, r in p.matches])

        total_points = 0

        for r in range(1, 5):
            row_matches = []

            for card, row_num in p.matches:
                if row_num == r:
                    row_matches.append(card)

            if len(row_matches) > 0:
                row_points = len(row_matches) * (5 - r)
                total_points += row_points
                print(f"Row {r} matches:", [str(c) for c in row_matches], row_points, "points")

        print("Score:", total_points)