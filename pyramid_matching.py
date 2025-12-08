def pyramid_round(deck, players):
    for p in players:
        p.matches = []
        
    row_sizes = [4, 3, 2, 1]
    row = 1

    for size in row_sizes:
        for i in range(size):   
            card = deck.pop()
            for p in players:
                for h in p.hand:
                    if h.rank == card.rank:
                        p.matches.append((card, row))
                        
                        p.add_score(row)
                    
                        break  
        
        row += 1