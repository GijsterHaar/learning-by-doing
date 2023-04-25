def description_poker_hand(user_input):
    chunk_size = 5
    rank_order_straight = ['A', '2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'J', 'Q', 'K', 'A']

    for rank in rank_order_straight:
        chunked_ranks = [rank_order_straight[rank:rank + chunk_size] for rank in range(0, 10)]
        chunked_ranks_straight_flush = [rank_order_straight[rank:rank + chunk_size] for rank in range(0, 9)]
        ranks_royal_flush = rank_order_straight[9:]
        ranks_royal_flush.sort()
    
    if not isinstance(user_input, str) or user_input == '' or len(user_input) < 14:
        return 'Invalid Input'
    
    frequency_ranks = {}
    ranks_list = [i[0:-1] for i in user_input.split()]
    ranks_list.sort()
    frequency_suits = {}
    suits_list = [i[-1] for i in user_input.split()]
    suits_list.sort()

    for suit in suits_list:
        if suit not in frequency_suits:
            frequency_suits[suit] = 0
        frequency_suits[suit] += 1

    if len(frequency_suits) == 1:
        if ranks_list == ranks_royal_flush:
            return 'Royal Flush'
        for hand in chunked_ranks_straight_flush:
            hand.sort()
            if hand == ranks_list:
                return 'Straight Flush'
        for hand in chunked_ranks:
            hand.sort()
            if hand != ranks_list:
                return 'Flush'

    for hand in chunked_ranks:
        hand.sort()
        if hand == ranks_list:
            return 'Straight'

    for rank in ranks_list:
        if rank not in frequency_ranks:
            frequency_ranks[rank] = 0
        frequency_ranks[rank] += 1
    return return_card_function(frequency_ranks, ranks_list)


def return_card_function(frequency_ranks, ranks_list):
    number_of_ranks = len(frequency_ranks)

    checks = ((check_for_four_of_a_kind, 'Four Of A Kind'),
              (check_for_full_house, 'Full House'),
              (check_for_three_of_a_kind, 'Three Of A Kind'),
              (check_for_two_pair, 'Two Pair'),
              (check_for_one_pair, 'One Pair'),
              (check_for_high_card, 'High Card'))
    
    for check_function, value in checks:
        if check_function(number_of_ranks, frequency_ranks):
            return_card = value
            break
    return return_card


def check_for_one_pair(number_of_ranks, frequency_ranks):
    return number_of_ranks == 4

def check_for_two_pair(number_of_ranks, frequency_ranks):
    return number_of_ranks == 3

def check_for_three_of_a_kind(number_of_ranks, frequency_ranks):
    return number_of_ranks == 3 and 3 in frequency_ranks.values()

def check_for_full_house(number_of_ranks, frequency_ranks):
    return number_of_ranks == 2

def check_for_four_of_a_kind(number_of_ranks, frequency_ranks):
    return number_of_ranks == 2 and 4 in frequency_ranks.values()

def check_for_high_card(number_of_ranks, frequency_ranks):
    return True

