from card import parse_card

def description_poker_hand(user_data):
    parsed_ranks = []
    parsed_suits = []
    rank_order_list = ['ace', '2', '3', '4', '5', '6', '7',
                   '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    chunk_size = 5
    rank_order_list_straight_flush = ['ace', '2', '3', '4', '5',
                                      '6', '7','8', '9', '10']
    rank_order_list_royal_flush = ['10', 'jack', 'queen', 'king', 'ace']

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
            for i in rank_order_list:
                chunked_lists_ranks = [rank_order_list[i:i + chunk_size] \
                                       for i in range(0, len(rank_order_list))]
                if len(chunked_lists_ranks) == 4:
                    break
            if parsed_ranks in chunked_lists_ranks and len(frequency_list_suits) > 1:
                return "Straight"
            
            if len(frequency_list_suits) == 1:
                for i in rank_order_list_straight_flush:
                    chunked_lists_suits = [rank_order_list_straight_flush[i:i + chunk_size] \
                                           for i in range(0, len(rank_order_list_straight_flush))]
                    if len(rank_order_list_straight_flush) == 4:
                        break

            if len(frequency_list_suits) == 1 and parsed_ranks == rank_order_list_royal_flush:
                return 'Royal Flush'        
            elif len(frequency_list_suits) == 1 and parsed_ranks in chunked_lists_suits:
                return 'Straight Flush'  
            elif len(frequency_list_suits) == 1:
                return 'Flush'
            else:
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




    

