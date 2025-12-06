def pyramid_round(deck, players):
    for p in players:
        p.matches = []

    for i in range(10):   
        card = deck.pop()
        for p in players:
            for h in p.hand:
                if h.rank == card.rank:
                    p.matches.append(card)
                    break  
