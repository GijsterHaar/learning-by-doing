def description_poker_hand(user_input):
    if not isinstance(user_input, str) or user_input == '' or len(user_input) < 14:
        return 'Invalid Input'
    
    frequency_ranks = {}
    ranks_list = [i[:1] for i in user_input.split()]
    for rank in ranks_list:

        if rank not in frequency_ranks:
            frequency_ranks[rank] = 0
        frequency_ranks[rank] += 1
    
    return return_card_function(frequency_ranks)

def return_card_function(frequency_ranks):
    number_of_ranks = len(frequency_ranks)
    # if check_for_one_pair(number_of_ranks, frequency_ranks):
    #     return_card = "One Pair"
    # elif check_for_three_of_a_kind(number_of_ranks, frequency_ranks):
    #     return_card = 'Three of a Kind'
    # elif check_for_two_pair(number_of_ranks, frequency_ranks):
    #     return_card = 'Two Pair'
    # else:
    #     return_card = "High Card"

    checks = ((check_for_three_of_a_kind, 'Three of a Kind'),
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

def check_for_high_card(number_of_ranks, frequency_ranks):
    return True

