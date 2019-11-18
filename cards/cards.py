
import random

class Card:
    """Standard playing card."""

    suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
    ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    def __init__(self, *argv):
        if len(argv) == 1:
            # Define by index (0-51)
            if argv[0] < 0 or argv[0] >= 52:
                raise IndexError
            self._suit = int(argv[0] / 13)
            self._rank = argv[0] % 13
        elif len(argv) == 2:
            pass
        else:
            pass 

    @property
    def rank(self):
        return self.ranks[self._rank]

    @property
    def suit(self):
        return self.suits[self._suit]

    def __repr__(self):
        return '{}{}'.format(self.suit[0], self.rank)

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __eq__(self, other):
        return (self._suit == other._suit and
                self._rank == other._rank)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self._rank < other._rank

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return self._rank > other._rank

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


class Deck:
    """Standard deck of cards."""

    def __init__(self, cards=52):
        '''Initialize a deck of card in standard order.'''
        self._cards = [Card(i) for i in range(cards)]

    def __repr__(self):
        pass

    def __str__(self):
        return '\n'.join([card.__str__() for card in self._cards])

    def __len__(self):
        return len(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self, cards=1):
        if not self._cards:
            return False
        return [self._cards.pop() for _ in range(cards)]

    def deal(self, cards=4, players=4):
        if cards * players > len(self._cards):
            return False
        return [self.draw(cards)]


class Hand:
    def __init__(self, cards):
        self.cards = cards

if __name__ == '__main__':
    # Unit test
    deck = Deck()
    deck.shuffle()
    print(deck)