from ranks import ranks

class Card:
    """
    Card object contains a colour and a symbol
    """
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
symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# ----- called by API -----

def update_cards(hand_cards: list, community_cards: list): 
    """
    Wrapper function, call this function for the API
    """
    hand_cards = convert_to_card_objects(hand_cards)
    community_cards = convert_to_card_objects(community_cards)
    get_hand_cards(hand_cards)
    get_community_cards(community_cards)
    covered_cards = update_covered_cards(hand_cards, community_cards)
    return create_combinations(hand_cards, community_cards, covered_cards)

# -------------------------

def get_card_index(card_list: list, searched_card: Card):
    """
    Returns the index of a card in a list
    """
    for i, card in enumerate(card_list):
        if card.colour == searched_card.colour and card.symbol == searched_card.symbol:
            return i
    return -1

def convert_to_card_objects(cards: list):
    """
    Changes representation of a card from a tuple to a card object
    """
    return [Card(colour, symbol) for colour, symbol in cards]

def get_hand_cards(hand_cards: list): 
    print("Hand cards:")
    for hand_card in hand_cards:
        print(hand_card)
    print()

def get_community_cards(community_cards: list): 
    print("Community cards:")
    for community_card in community_cards:
        print(community_card)
    print()

def update_covered_cards(hand_cards: list, community_cards: list):
    """
    Remove revealed cards (hand cards and community cards) from the stack of all cards
    """
    cards = [Card(colour, symbol) for colour in colours for symbol in symbols]

    for card in hand_cards:
        cards.pop(get_card_index(cards, card))  
    for card in community_cards:
        cards.pop(get_card_index(cards, card))  
    return cards

def create_combinations(hand_cards: list, community_cards: list, covered_cards: list):
    """
    Creates all possible card combinations for each stage (Flop, Turn, River) to determine the probabilities
    """
    uncovered_cards = hand_cards + community_cards
    card_combinations = []

    if len(hand_cards) == 2 and len(community_cards) >= 3:
        # Flop
        if len(community_cards) == 3:
            for i in range(len(covered_cards)):
                for j in range(i + 1, len(covered_cards)):
                    card_combinations.append((uncovered_cards[0], uncovered_cards[1], uncovered_cards[2], uncovered_cards[3], uncovered_cards[4], covered_cards[i], covered_cards[j]))
        # Turn
        elif len(community_cards) == 4:
            for i in range(len(covered_cards)):
                card_combinations.append((uncovered_cards[0], uncovered_cards[1], uncovered_cards[2], uncovered_cards[3], uncovered_cards[4], uncovered_cards[5], covered_cards[i]))
        # River
        elif len(community_cards) == 5:
            card_combinations = [(uncovered_cards[0], uncovered_cards[1], uncovered_cards[2], uncovered_cards[3], uncovered_cards[4], uncovered_cards[5], uncovered_cards[6])]

        return ranks(card_combinations)
    else:
        return {"Straight Flush": "0.0%", "Four-of-a-Kind": "0.0%", "Full House": "0.0%", "Flush": "0.0%", "Straight": "0.0%", "Three-of-a-Kind": "0.0%", "Two Pair": "0.0%", "Pair": "0.0%", "Highest Card": "0.0%"}




