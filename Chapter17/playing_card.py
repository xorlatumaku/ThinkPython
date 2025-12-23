# Date: 06/12/2025
# Program to implement playing cards

import random

# Cards
class Card:
    """ Represents a standard playing card."""
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        rank_name = Card.rank_names[self.rank]
        suit_name = Card.suit_names[self.suit]
        return f'{rank_name} of {suit_name}'
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    def to_tuple(self):
        return (self.suit, self.rank)
    def __lt__(self, other):
        return self.to_tuple() < other.to_tuple()
    def __le__(self, other):
        return self.to_tuple() <= other.to_tuple()

# Decks
class Deck:
    def __init__(self, cards):
        self.cards = cards
    def make_cards():
        cards = []
        for suit in range(4):
            for rank in range(2, 15):
                card = Card(suit, rank)
                cards.append(card)
        return cards
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
            return '\n'.join(res)
    def take_card(self):
        return self.cards.pop()
    def put_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
    def move_cards(self, other, num):
        for i in range(num):
            card = self.take_card()
            other.put_card(card)

# Hand
class Hand(Deck):
    """ Represents a hand of playing cards. """
    def __init__(self, label=''):
        self.label = label
        self.cards = []

# BridgeHand
class BridgeHand(Hand):
    """ Represents a bridge hand."""

    hcp_dict = {
            'Ace': 4,
            'King': 3,
            'Queen': 2,
            'Jack':1,
    }
    def high_card_point_count(self):
        count = 0
        for card in self.cards:
            rank_name = Card.rank_names[card.rank]
            count += BridgeHand.hcp_dict.get(rank_name, 0)
        return count
    
print(Card.suit_names)
print(Card.suit_names[0])
print(Card.rank_names[11])

queen = Card(1, 12)
print(queen.suit, queen.rank)
print(queen.suit_names)
print()

print(queen)

# Comparing cards
queen2 = Card(1, 12)
print(queen2)
print(queen == queen2)

six = Card(1, 6)
print(six)

print(queen == six)
print(queen != queen2)
print(queen != six)
print(six < queen)
print(queen < queen2)
print(queen > queen2)
print(queen <= queen2)
print(queen <= six)
print(queen >= six)
print()

cards = Deck.make_cards()
deck = Deck(cards)
print(len(deck.cards))
small_deck = Deck([queen, six])
print(small_deck)
print()

card = deck.take_card()
print(card)
print(len(deck.cards))
print()

deck.put_card(card)
print(len(deck.cards))
print()

deck.shuffle()
for card in deck.cards[:4]:
    print(card)
print()

for card in deck.cards[:4]:
    print(card)
print()

# Deal a card
hand = Hand('player 1')
print(hand.label)
print()

deck = Deck(cards)
card = deck.take_card()
hand.put_card(card)
print(hand)
print()

rank = 12
rank_name = Card.rank_names[rank]
score = BridgeHand.hcp_dict.get(rank_name, 0)
print(rank_name, score)
print()

hand = BridgeHand('player 2')
deck.shuffle()
deck.move_cards(hand, 5)
print(hand)
print()

hand.high_card_point_count()
