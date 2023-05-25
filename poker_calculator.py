import random
import itertools
from bs4 import BeautifulSoup
from  selenium import webdriver
import poker_hands as ph

# TO DOS: Fehler mit Pop out of Index fixen
# !!!!! anscheinend straße auch mit Ass beginnend möglich

class Card:
    def __init__(self, colour, symbol):
        self.colour = colour
        self.symbol = symbol
    
    def get_colour(self):
        return self.colour

    def get_symbol(self):
        return self.symbol

    def __str__(self):
        return f"{self.symbol} of {self.colour}"

colours = ["Hearts", "Diamonds", "Clubs", "Spades"]
symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# ----- Hilfsfunktionen -----

# ----- Erzeugung aller Karten -----
cards = []

for i in colours:
    for j in symbols:
        cards.append(Card(i, j))
# ----------------------------------


# ----- Kartenverteilung -----

# ----- Handkarten -----
covered_cards = cards.copy()
my_cards = []
for i in range(2):
    my_cards.append(covered_cards.pop(random.randint(0, len(covered_cards))))
print("My Cards:")
for card in my_cards:
    print(card)
# ----------------------

known_cards = my_cards.copy()

# ----- Flop -----
flop = []
for i in range(3):
    flop.append(covered_cards.pop(random.randint(0, len(covered_cards))))
print("Flop:")
for card in flop:
    print(card)

known_cards = my_cards + flop

# ----- Alle möglichen Kombinationen nach dem Flop -----
card_combinations = []

for i in range(len(covered_cards)): # 2 Handkarten, 3 Flopkarten, 2 Verbleibende --> alle möglichen Kombinationen in einem 7-Tupel
    for j in range(i + 1, len(covered_cards)):
        card_combinations.append((known_cards[0], known_cards[1], known_cards[2], known_cards[3], known_cards[4], covered_cards[i], covered_cards[j]))

# Ausgabe aller Kombinationen, wenn gewünscht
# for i in range(len(card_combinations)): # Mögliche Kombinationen aller Karten
#     for j in range(7): # 7-Tupel
#         print(card_combinations[i][j], " ", end="") # erster Index: Tupel in Liste, zweiter Index: Element innerhalb des Tupels
#     print("\n")

ph.ranks(card_combinations)
# ------------------------------------------------------
# ----------------

# ----- Turn -----
turn = flop.copy()
turn.append(covered_cards.pop(random.randint(0, len(covered_cards))))
print("Turn:")
for card in turn:
    print(card)

known_cards = my_cards + turn

# ----- Alle möglichen Kombinationen nach dem Turn -----
card_combinations = []

for i in range(len(covered_cards)): # 2 Handkarten, 4 Turnkarten, 1 Verbleibende --> alle möglichen Kombinationen in einem 7-Tupel
    card_combinations.append((known_cards[0], known_cards[1], known_cards[2], known_cards[3], known_cards[4], known_cards[5], covered_cards[i]))

# Ausgabe aller Kombinationen, wenn gewünscht
# for i in range(len(card_combinations)): # Mögliche Kombinationen aller Karten
#     for j in range(7): # 7-Tupel
#         print(card_combinations[i][j], " ", end="") # erster Index: Tupel in Liste, zweiter Index: Element innerhalb des Tupels
#     print("\n")

ph.ranks(card_combinations)
# -------------------------------------------------------
# -----------------
 
# ----- River -----
river = turn.copy()
river.append(covered_cards.pop(random.randint(0, len(covered_cards))))
print("River:")
for card in river:
    print(card)
known_cards = my_cards + river

card_combinations = [(known_cards[0], known_cards[1], known_cards[2], known_cards[3], known_cards[4], known_cards[5], known_cards[6])]

# Ausgabe aller Kombinationen, wenn gewünscht
# for i in range(len(card_combinations)): # Mögliche Kombinationen aller Karten
#     for j in range(7): # 7-Tupel
#         print(card_combinations[i][j], " ", end="") # erster Index: Tupel in Liste, zweiter Index: Element innerhalb des Tupels
#     print("\n")

ph.ranks(card_combinations)
# ----------------




# ----------------------------



