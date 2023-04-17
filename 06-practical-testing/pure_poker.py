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
            frequency_list_ranks = frequency_dict(parsed_ranks)

        if len(frequency_list_ranks) == 5:
            return 'High Card'
        elif len(frequency_list_ranks) == 4:
            return 'One Pair'
        elif len(frequency_list_ranks) == 3:
            for freq in frequency_list_ranks:
                if freq == 3:
                    return 'Three Of A Kind'
                else:
                    return 'Two Pair'
        elif len(frequency_list_ranks) == 2:
            for freq in frequency_list_ranks:
                if freq == 4:
                    return 'Four Of A Kind'
                else:
                    return 'Full House'

def frequency_dict(parsed_ranks):
    frequency_dict = {}
    frequency_list_ranks = []
    for rank in parsed_ranks:
        if rank not in frequency_dict:
            frequency_dict[rank] = 1
        else:
            frequency_dict[rank] += 1
    for rank in frequency_dict:
        frequency_list_ranks.append(frequency_dict[rank])
    return frequency_list_ranks



    

