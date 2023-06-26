
def description_rummy_hand(user_input):
    suits = ['H', 'C', 'D', 'S']
    rank_order_straight = ['1', '2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'J', 'Q', 'K']
    # chunk_size = [3, 4]
    # for rank in rank_order_straight:
    #     chunked_ranks_three = [rank_order_straight[rank:rank + chunk_size[0]] for rank in range(0, 11)]
    #     chunked_ranks_three.sort()
    #     chunked_ranks_four = [rank_order_straight[rank:rank + chunk_size[1]] for rank in range(0, 10)]
    #     chunked_ranks_four.sort()

    if not isinstance(user_input, str) or user_input == '' or len(user_input) < 20:
        return 'INVALID'
    user_input = user_input.upper()

    frequency_ranks = {}
    ranks_list = [i[0:-1] for i in user_input.split()]
    if not len(ranks_list) == 7:
        return 'INVALID'
    ranks_list.sort()
    frequency_ranks = {}
    ranks_list = [i[0:-1] for i in user_input.split()]
    if not len(ranks_list) == 7:
        return 'INVALID'
    ranks_list.sort()
    for _ in range(7):
        if ranks_list[-1] == "A":
            ranks_list[-1] = '1'
        ranks_list.sort()

    frequency_suits = {}
    suit_list = [i[-1] for i in user_input.split()]
    for suit in suit_list:
        if not suit in suits:
            return 'INVALID'

    for rank in ranks_list:
        if rank not in frequency_ranks:
            frequency_ranks[rank] = 0
        frequency_ranks[rank] += 1
    
    for suit in suit_list:
        if suit not in frequency_suits:
            frequency_suits[suit] = 0
        frequency_suits[suit] += 1

    if len(frequency_ranks) == 2 and 4 in frequency_ranks.values():
        return "WIN"
    return "LOSE"


