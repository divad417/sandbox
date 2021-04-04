"""
Define a deck of cards.

"""

class Card:
    """ Standard playing card. """

    suit_names = ('S', 'D', 'C', 'H')
    rank_names = (None, 'A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    suit_names_long = ('Spades', 'Diamonds', 'Clubs', 'Hearts')
    rank_names_long = (None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank
        self.indx = 13 * suit + rank

    def __repr__(self):
        return '%s%s' %  (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __str__(self):
        return '%s of %s' % (Card.rank_names_long[self.rank], Card.suit_names_long[self.suit])

    def __eq__(self, other):
        return self.indx == other.indx

    def __ne__(self, other):
        return not self.__eq__(other)
