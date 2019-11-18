#!/usr/local/bin/python3

from cards import *


def play_solitaire():
    """ Play single deck solitaire. """
    deck = Deck()
    deck.shuffle()
    hand = deck.draw(4)
    count = 0

    while True:
        if len(hand) < 4:
            if len(deck):
                hand += deck.draw()
                continue
            elif len(hand) == 0:
                return 'Win'
            elif count < 4:
                hand += [hand.pop(0)]
                count += 1
            else:
                return 'Lose'

        if hand[0].rank == hand[3].rank:
            del hand[0:4]
            count = 0
            continue

        if hand[0].suit == hand[3].suit:
            del hand[1:3]
            count = 0
            continue
    

if __name__ == '__main__':
    results = {'Win': 0,
               'Draw': 0,
               'Lose': 0}
    
    for _ in range(1000):
        results[play_solitaire()] +=1

    print(results)

# {'Win': 70, 'Draw': 521, 'Lose': 409}
# {'Win': 750, 'Draw': 5138, 'Lose': 4112}
# {'Win': 780, 'Draw': 5033, 'Lose': 4187}
# {'Win': 768, 'Draw': 5016, 'Lose': 4216}
# {'Win': 7588, 'Draw': 50826, 'Lose': 41586}
# {'Win': 76423, 'Draw': 505194, 'Lose': 418383}