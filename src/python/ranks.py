def ranks(card_combinations: list):
    """
    Gets all possible card combinations as a 7-tuple and calculates the probability for each rank
    If there is an occurance of a rank that is covered by a higher rank, it will not be listed
    """
    occurances = {"Straight Flush": 0, "Four-of-a-Kind": 0, "Full House": 0, "Flush": 0, "Straight": 0, "Three-of-a-Kind": 0, "Two Pair": 0, "Pair": 0, "Highest Card": 0}
    is_rank = {"Straight Flush": False, "Four-of-a-Kind": False, "Full House": False, "Flush": False, "Straight": False, "Three-of-a-Kind": False, "Two Pair": False, "Pair": False}

    def straight_flush(cards: tuple):
        colours = get_colours(cards)
        counter = 0
        flush_colour = ""
        straight_flush = []
            
        for colour in colours:
            if colours.count(colour) >= 5:
                flush_colour = colour
                break
        
        # add all flush cards to later check if it is a straight
        for card in cards:
            if card.get_colour() == flush_colour:
                straight_flush.append(card)

        straight_flush = get_symbols(sorted(straight_flush, key=lambda card: card.get_symbol()))

        # check if it is a "A, 2, 3, 4, 5" straight
        # sum of 2, 3, 4, 5 equals 14
        if len(straight_flush) >= 5 and straight_flush[-1] == 14: 
            sum = 0
            for i in range(4):
                sum += straight_flush[i]
            if sum == 14: 
                occurances["Straight Flush"] += 1
                is_rank["Straight Flush"] = True
                return   

        # no duplicates in straight_flush list
        # if it is a straight, 5 consecutive cards must have difference of 1
        for i in range(len(straight_flush) - 1):
                if straight_flush[i + 1] - straight_flush[i] == 1:
                    counter += 1
                else: 
                    counter = 0

                if counter == 4: 
                    occurances["Straight Flush"] += 1
                    is_rank["Straight Flush"] = True
                    return
                else:
                    is_rank["Straight Flush"] = False

    def four_of_a_kind(symbols: list):
        if is_rank["Straight Flush"] == False:
            for symbol in symbols:
                if symbols.count(symbol) == 4: 
                    occurances["Four-of-a-Kind"] += 1
                    is_rank["Four-of-a-Kind"] = True
                    return
                else:
                    is_rank["Four-of-a-Kind"] = False
    
    def full_house(symbols: list):
        if is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False:
            full_house = set()
            num_of_triples = 0
            for symbol in symbols:
                if symbols.count(symbol) == 2:
                    full_house.add(symbol)
                if symbols.count(symbol) == 3:
                    full_house.add(symbol)
                    num_of_triples += 1

            # Full House must contain at least one triple
            if len(full_house) >= 2 and num_of_triples >= 1: 
                occurances["Full House"] += 1
                is_rank["Full House"] = True
            else:
                is_rank["Full House"] = False

    def flush(colours: list):
        if is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False and is_rank["Full House"] == False:
            for colour in colours:
                if colours.count(colour) >= 5: 
                    occurances["Flush"] += 1
                    is_rank["Flush"] = True
                    return
                else:
                    is_rank["Flush"] = False

    def straight(symbols: list):
        if is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False and is_rank["Full House"] == False and is_rank["Flush"] == False:
            counter = 0
            straight = set()
            for symbol in symbols:
                straight.add(symbol)
            
            straight = sorted(straight, key=int)

            # check if it is a "A, 2, 3, 4, 5" straight
            # sum of 2, 3, 4, 5 equals 14
            if len(straight) >= 5 and straight[-1] == 14:
                sum = 0
                for i in range(4):
                    sum += straight[i]
                if sum == 14: 
                    occurances["Straight"] += 1
                    is_rank["Straight"] = True
                    return                  

            # if it is a straight, 5 consecutive cards must have difference of 1
            for i in range(len(straight) - 1):
                if straight[i + 1] - straight[i] == 1:
                    counter += 1
                else: 
                    counter = 0
    
                if counter == 4: 
                    occurances["Straight"] += 1
                    is_rank["Straight"] = True
                    return
                else:
                    is_rank["Straight"] = False

    def three_of_a_kind(symbols: list):
        if is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False and is_rank["Full House"] == False and is_rank["Flush"] == False and is_rank["Straight"] == False:
            for symbol in symbols:
                if symbols.count(symbol) == 3:
                    occurances["Three-of-a-Kind"] += 1
                    is_rank["Three-of-a-Kind"] = True
                    return
                else:
                    is_rank["Three-of-a-Kind"] = False

    def two_pair(symbols: list):
        if is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False and is_rank["Full House"] == False and is_rank["Flush"] == False and is_rank["Straight"] == False and is_rank["Three-of-a-Kind"] == False:
            pairs = set()
            for symbol in symbols:
                if symbols.count(symbol) == 2:
                    pairs.add(symbol)
            
            if len(pairs) >= 2:
                occurances["Two Pair"] += 1
                is_rank["Two Pair"] = True
            else:
                is_rank["Two Pair"] = False

    def pair(symbols: list):
        if is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False and is_rank["Full House"] == False and is_rank["Flush"] == False and is_rank["Straight"] == False and is_rank["Three-of-a-Kind"] == False and is_rank["Two Pair"] == False:
            for symbol in symbols:
                if symbols.count(symbol) == 2:
                    occurances["Pair"] += 1
                    is_rank["Pair"] = True
                    return
                else:
                    is_rank["Pair"] = False

    def highest_card():
        for rank in is_rank:
            if is_rank[rank] == True:
                return
        occurances["Highest Card"] += 1
    

    for cards in card_combinations:
        cards = convert_symbols_to_values(cards)
        symbols = get_symbols(cards)
        colours = get_colours(cards)
        straight_flush(cards)
        four_of_a_kind(symbols)
        full_house(symbols)
        flush(colours)
        straight(symbols)
        three_of_a_kind(symbols)
        two_pair(symbols)
        pair(symbols)
        highest_card()

    percentages = occurances.copy()

    for rank in occurances.keys():
            percentages[rank] = str(round((percentages[rank]/len(card_combinations)) * 100, 2)) + "%"
    print(percentages)
    return percentages

def convert_symbols_to_values(cards: tuple):
    """
    Converts the symbols from 1-10 and especially J, Q, K and A to integers
    """
    for card in cards:
        if card.get_symbol() == "J":
            card.symbol = 11
        elif card.get_symbol() == "Q":
            card.symbol = 12
        elif card.get_symbol() == "K":
            card.symbol = 13
        elif card.get_symbol() == "A":
            card.symbol = 14
        else:
            card.symbol = int(card.symbol)
    return cards

def get_symbols(cards: tuple):
    """
    Extracts the symbols from each card object of a 7-tuple
    """
    symbols = []
    for card in cards:
        symbols.append(card.get_symbol())
    return symbols

def get_colours(cards: tuple):
    """
    Extracts the colours from each card object of a 7-tuple
    """
    colours = []
    for card in cards:
        colours.append(card.get_colour())
    return colours