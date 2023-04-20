from card import parse_card
from itertools import permutations

def description_poker_hand(user_data):
    rank_order_straight = ['ace', '2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    rank_order_straight_flush = rank_order_straight[:-1]
    rank_order_royal_flush = rank_order_straight[9:]
    parsed_ranks = []
    parsed_suits = []
    chunk_size = 5

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
            frequency_list_ranks = counting_rank_dict(parsed_ranks)
            frequency_list_suits = counting_suit_dict(parsed_suits)

    if len(frequency_list_ranks) == 5:
        for i in rank_order_straight:
            chunked_ranks = [rank_order_straight[i:i + chunk_size] \
                             for i in range(10)]
            for chunked in chunked_ranks:
                possible_list = get_possibles(chunked)
                for all_possibles in possible_list:
                    if parsed_ranks == all_possibles and len(frequency_list_suits) > 1:
                        return 'Straight'

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

def counting_rank_dict(parsed_ranks):
    frequency_dict_ranks = {}
    frequency_list_ranks = []
    for rank in parsed_ranks:
        if rank not in frequency_dict_ranks:
            frequency_dict_ranks[rank] = 1
        else:
            frequency_dict_ranks[rank] += 1    
    for rank in frequency_dict_ranks:
        frequency_list_ranks.append(frequency_dict_ranks[rank])
    return frequency_list_ranks

def counting_suit_dict(parsed_suits):
    frequency_dict_suits = {}
    frequency_list_suits = []
    for suit in parsed_suits:
        if suit not in frequency_dict_suits:
            frequency_dict_suits[suit] = 1
        else:
            frequency_dict_suits[suit] += 1
    for rank in frequency_dict_suits:
        frequency_list_suits.append(frequency_dict_suits[suit])
    return frequency_list_suits

def get_possibles(chunked):
    possible_list = []
    possibles = list(permutations(chunked))
    for possible in possibles:
        possible =(list(possible))
        possible_list.append(possible)
    return possible_list