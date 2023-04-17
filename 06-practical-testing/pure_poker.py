from card import parse_card

def description_poker_hand(user_data):
    parsed_ranks = []
    parsed_suits = []
    if user_data == '' or not (isinstance(user_data,str)) or len(user_data.split()) != 5:
        return "Sorry, that's invalid"
    else:
        for c in user_data.split():
            try:
                card = parse_card(c)
            except ValueError:
                return "Sorry, that's invalid"
            
            parsed_ranks.append(card['rank'])
            parsed_suits.append(card['suit'])
            frequency_list = frequency_dict(parsed_ranks)

        if len(frequency_list) == 5:
            return 'High Card'
        elif len(frequency_list) == 4:
            return 'One Pair'
        elif len(frequency_list) == 3:
            for freq in frequency_list:
                if freq == 3:
                    return 'Three Of A Kind'
                else:
                    return 'Two Pair'
    # return frequency_list

def frequency_dict(parsed_ranks):
    frequency_dict = {}
    frequency_list = []
    for rank in parsed_ranks:
        if rank not in frequency_dict:
            frequency_dict[rank] = 1
        else:
            frequency_dict[rank] += 1
    for rank in frequency_dict:
        frequency_list.append(frequency_dict[rank])
    return frequency_list




        # return parsed_ranks, parsed_suits


    

