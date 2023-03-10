import random

SUITS = ["Diamonds", "Hearts", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Card():
  """Class to make and return cards"""
  def __init__(self, new_rank, new_suit):
    self.rank = new_rank
    self.suit = new_suit

def __repr__(self):
    return self.rank + " of " + self.suit

deck = []
for suit in SUITS:
    for rank in RANKS:
        deck.append(Card(rank, suit))
random.shuffle(deck)

p1 = deck[0:5]

ranks_list = {}
for suit in SUITS:
    ranks_list[suit] = 0

for card in p1:
    ranks_list[card.suit] += 1

ranks_list = list(ranks_list.values())
flush = True

for card in p1:
    if p1[0].suit != card.suit:
        flush = False  

if ranks_list == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1] and flush:
    print("royal flush")
elif flush and str(ranks_list).count("11111") == 1:
    print("straight flush")
elif ranks_list.count(4) == 1:
    print("four of a kind")
elif ranks_list.count (2) == 1 and ranks_list.count(3) == 1:
    print("full house")
elif flush:
    print("flush")
elif str(ranks_list).count("11111") == 1:
    print("straight")
elif ranks_list.count(3) == 1:
  print("Three of a kind!!!")
elif ranks_list.count(2) == 2:
    print("two pair")
elif ranks_list.count(2) == 1:
  print("one pair!!!")
else:
  print("Garbage")





            