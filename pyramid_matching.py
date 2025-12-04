def pyramid_round(deck, hand):
    matches = []

    for i in range(10):
        card = deck.pop()
        for h in hand:
            if h.rank == card.rank:
                matches.append(card)
                break

    print("Number of matches in pyramid round: ", len(matches))
    return matches
