"""
Program to play deck-in-hand solitaire and analyze statistics.

"""
import random
from color import color

class Card:
    """ Standard playing card. """

    suit_names = ['S', 'D', 'C', 'H']
    rank_names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suit_names_long = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
    rank_names_long = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, indx=0):
        self.indx = indx
        self.suit = self.indx / 13
        self.rank = self.indx % 13

    def __repr__(self):
        return '%s%s' %  (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __str__(self):
        return '%s of %s' % (Card.rank_names_long[self.rank], Card.suit_names_long[self.suit])

    def __eq__(self, other):
        return self.indx == other.indx

    def __ne__(self, other):
        return not self.__eq__(other)

class Deck:
    """ Deck of cards. """

    def __init__(self):
        self.deck_order = range(51)
        self.deck = [Card(i) for i in self.deck_order]
        self.hand_order = []
        self.status = 'Playing'
        self.count = 0

    def __getitem__(self, key):
        return self.deck[key]

    def shuffle(self):
        random.shuffle(self.deck_order)

    def draw(self):
        if len(self.deck_order) > 0:
            self.hand_order.insert(0, self.deck_order.pop())
            self.deck = [Card(i) for i in self.hand_order]

    def compare(self):
        a = self.deck[0]
        b = self.deck[3]
        if a.suit == b.suit:
            del self.deck[1:3]
            del self.hand_order[1:3]
            print color.CYAN + str(self.deck) + color.END
        if a.rank == b.rank:
            del self.deck[0:4]
            del self.hand_order[0:4]
            print color.PURPLE + str(self.deck) + color.END

    def check(self):
        if len(self.deck_order) == 0:
            if len(self.deck)== 0:
                self.status = 'True Win!'
            elif len(self.deck) == 2:
                self.status = 'Psudo Win'
            else:
                self.hand_order.insert(0, self.hand_order.pop())
                self.deck = [Card(i) for i in self.hand_order]
                self.count += 1
                if self.count == 3:
                    self.status = 'Lose'




def solitaire():
    """ Play single deck solitaire. """
    deck = Deck()
    deck.shuffle()

    while deck.status == 'Playing':
        deck.draw()
        while len(deck.hand_order) < 4:
            deck.draw()
        print deck.deck

        deck.compare()
        deck.check()
    
    return deck.status


print solitaire()