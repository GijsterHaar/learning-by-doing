from card import parse_card

def description_poker_hand(user_data):

    rank_order_straight = ['ace', '2', '3', '4', '5', '6', '7',
                   '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    rank_order_straight_flush = rank_order_straight[:-1]
    rank_order_royal_flush = rank_order_straight[9:]
    rank_order_royal_flush.sort()
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
            parsed_ranks.sort()
            parsed_suits.append(card['suit'])
            parsed_suits.sort()
            frequency_list_ranks = counting_rank_dict(parsed_ranks)
            frequency_list_suits = counting_suit_dict(parsed_suits)


        if len(frequency_list_ranks) == 5: 
            for rank in rank_order_straight:
                chunked_lists_ranks = [rank_order_straight[rank:rank + chunk_size] for rank in range(0, 10)]
                for rank in chunked_lists_ranks:
                    rank.sort()

            if parsed_ranks in chunked_lists_ranks and len(frequency_list_suits) > 1:
                return "Straight"
            
            if len(frequency_list_suits) == 1:
                for rank in rank_order_straight_flush:
                    chunked_lists_straight_flush= [rank_order_straight_flush[rank:rank + chunk_size] for rank in range(0, 9)]
                    for rank in chunked_lists_straight_flush:
                        rank.sort()
                        if parsed_ranks == rank:
                            return 'Straight Flush'
                if parsed_ranks == rank_order_royal_flush:
                    return 'Royal Flush'
                return 'Flush'
            else:
                return 'High Card'
            
        elif len(frequency_list_ranks) == 4:
            return 'One Pair'
        elif len(frequency_list_ranks) == 3 and 3 in frequency_list_ranks:
            return 'Three Of A Kind'
        elif len(frequency_list_ranks) == 3 and 2 in frequency_list_ranks:
            return 'Two Pair'
        elif len(frequency_list_ranks) == 2 and 4 in frequency_list_ranks:
            return 'Four Of A Kind'
        elif len(frequency_list_ranks) == 2 and 3 in frequency_list_ranks:
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




    

