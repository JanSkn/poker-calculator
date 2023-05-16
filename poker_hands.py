
def symbol_converter(tuple):
    temp_values = []
    for i in range(len(tuple)):
        if tuple[i].symbol == "Jack":
            temp_values.append("11")
        elif tuple[i].symbol == "Queen":
            temp_values.append("12")
        elif tuple[i].symbol == "King":
            temp_values.append("13")
        elif tuple[i].symbol == "Ace":
            temp_values.append("14")
        else:
            temp_values.append(tuple[i].symbol)
    return temp_values

def colour_converter(tuple):
    temp_values = []
    for i in range(len(tuple)):
        temp_values.append(tuple[i].colour)
    return temp_values

def ranks(card_combinations):
    occurances = {"Straight Flush": 0, "Four-of-a-Kind": 0, "Full House": 0, "Flush": 0, "Straight": 0, "Three-of-a-Kind": 0, "Two Pair": 0, "Pair": 0, "Highest Card": 0}
    is_rank = {"Straight Flush": False, "Four-of-a-Kind": False, "Full House": False, "Flush": False, "Straight": False, "Three-of-a-Kind": False, "Two Pair": False, "Pair": False}

    def straight_flush(symbol_list, colour_list):
        build_tuples = []
        bools = {"Is Flush": False, "Is Straight": False}
        for i in range(7):
            build_tuples.append((int(symbol_list[i]), colour_list[i]))

        # ----- Flush -----
        build_flush = []
        counter = 0
        for i in ["Hearts", "Spades", "Clubs", "Diamonds"]:
            for tup in build_tuples:
                for elem in tup:
                    if elem == i:
                        counter += 1
            if counter >= 5:
                bools["Is Flush"] = True
                for j in build_tuples:
                    if j[1] == i:
                        build_flush.append(j)
                break
            else:
                bools["Is Flush"] = False
            counter = 0
        sorted_flush = sorted(build_flush, key=lambda x: x[0])
        # -----------------

        # ----- Straight -----
        if bools["Is Flush"] == True:
            counter = 0
            building_straight = []
            for i in sorted_flush:
                if i not in building_straight:
                    building_straight.append(i)
            for k in range(len(building_straight) - 1):
                if (int(building_straight[k + 1][0]) - int(building_straight[k][0])) == 1:
                    counter += 1
                elif (int(building_straight[k + 1][0]) - int(building_straight[k][0])) > 1: 
                    counter = 0
                if counter >= 4:
                    bools["Is Straight"] = True
                    break
                else:
                    bools["Is Straight"] = False

        if bools["Is Flush"] == True and bools["Is Straight"] == True:
            occurances["Straight Flush"] += 1
            is_rank["Straight Flush"] = True
        # --------------------

    def four_of_a_kind(list):
        for i in list:
            if list.count(i) == 4 and is_rank["Straight Flush"] == False:
                occurances["Four-of-a-Kind"] += 1
                is_rank["Four-of-a-Kind"] = True
                break
            else:
                is_rank["Four-of-a-Kind"] = False
    
    def full_house(list):
        number_of_parts = []
        number_of_triples = 0
        for i in list:
            if list.count(i) == 2 and i not in number_of_parts:
                number_of_parts.append(i)
            if list.count(i) == 3 and i not in number_of_parts:
                number_of_parts.append(i) 
                number_of_triples += 1 
        if len(number_of_parts) >= 2 and number_of_triples >= 1 and is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False:
            occurances["Full House"] += 1
            is_rank["Full House"] = True
        else:
            is_rank["Full House"] = False

    def flush(list):
        for i in list:
            if list.count(i) >= 5 and is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False and is_rank["Full House"] == False:
                occurances["Flush"] += 1
                is_rank["Flush"] = True
                break
            else:
                is_rank["Flush"] = False

    def straight(list):
        counter = 0
        building_straight = []
        for i in list:
            if i not in building_straight:
                building_straight.append(i)
        building_straight.sort(key = int)
        for k in range(len(building_straight) - 1):
            if (int(building_straight[k + 1]) - int(building_straight[k])) == 1:
                counter += 1
            elif (int(building_straight[k + 1]) - int(building_straight[k])) > 1: 
                counter = 0
            if counter >= 4 and is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False and is_rank["Full House"] == False and is_rank["Flush"] == False:
                occurances["Straight"] += 1
                is_rank["Straight"] = True
                break
            else:
                is_rank["Straight"] = False

    def three_of_a_kind(list):
        number_of_triples = []
        for i in list:
            if list.count(i) == 3 and i not in number_of_triples:
                number_of_triples.append(i)
        if len(number_of_triples) == 1 and is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False and is_rank["Full House"] == False and is_rank["Flush"] == False and is_rank["Straight"] == False:
            occurances["Three-of-a-Kind"] += 1
            is_rank["Three-of-a-Kind"] = True
        else:
            is_rank["Three-of-a-Kind"] = False

    def two_pair(list):
        number_of_pairs = []
        for i in list:
            if list.count(i) == 2 and i not in number_of_pairs:
                number_of_pairs.append(i)
        if len(number_of_pairs) >= 2 and is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False and is_rank["Full House"] == False and is_rank["Flush"] == False and is_rank["Straight"] == False and is_rank["Three-of-a-Kind"] == False:
            occurances["Two Pair"] += 1
            is_rank["Two Pair"] = True
        else:
            is_rank["Two Pair"] = False

    def pair(list):
        number_of_pairs = []
        for i in list:
            if list.count(i) == 2 and i not in number_of_pairs:
                number_of_pairs.append(i)
        if len(number_of_pairs) == 1 and is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False and is_rank["Full House"] == False and is_rank["Flush"] == False and is_rank["Straight"] == False and is_rank["Three-of-a-Kind"] == False and is_rank["Two Pair"] == False:
            occurances["Pair"] += 1
            is_rank["Pair"] = True
        else:
            is_rank["Pair"] = False

    def highest_card():
        if is_rank["Straight Flush"] == False and is_rank["Four-of-a-Kind"] == False and is_rank["Full House"] == False and is_rank["Flush"] == False and is_rank["Straight"] == False and is_rank["Three-of-a-Kind"] == False and is_rank["Two Pair"] == False and is_rank["Pair"] == False:
            occurances["Highest Card"] += 1
    # ------------
    for i in range(len(card_combinations)):
        converted_symbols = symbol_converter(card_combinations[i])
        converted_colours = colour_converter(card_combinations[i])
        straight_flush(converted_symbols, converted_colours)
        four_of_a_kind(converted_symbols)
        full_house(converted_symbols)
        flush(converted_colours)
        straight(converted_symbols)
        three_of_a_kind(converted_symbols)
        two_pair(converted_symbols)
        pair(converted_symbols)
        highest_card()

    percentages = occurances.copy()
    for i in occurances.keys():
            percentages[i] = round((percentages[i]/len(card_combinations)) * 100, 2)
    print(percentages)
    return percentages