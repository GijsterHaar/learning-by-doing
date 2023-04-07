
def parse_card(input):

    suit_dict = {'C': 'clubs', 'D': 'diamonds', 'H': 'hearts', 'S': 'spades'}
    rank_dict_low = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
                  '9': '9', '10': '10'}
    rank_dict_high = {'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'}
    description_rank_dict = {'2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six',
                             '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}
    card_dict = {}

    if input == '':
        raise ValueError('Sorry mate, no input means no output')
    
    elif input == input.lower():
        raise ValueError('This is no valid choice, use capital')
    
    elif len(input) < 2 or len(input )> 3:
        raise ValueError('You did not enter the correct amount of characters')
     
    elif len(input) == 2:
        entered_suit = input[1:]
        entered_card = input[0:1]
        ranks_low = list(rank_dict_low.keys())
        ranks_high = list(rank_dict_high.keys())
        number_to_word = list(description_rank_dict.keys())
        suits = list(suit_dict.keys())
        if entered_suit not in suits:
            raise ValueError('Sorry mate, thats not a known suit in a deck')
        else:
            card_dict['suit'] = suit_dict[entered_suit]
            output_suit = card_dict['suit']
        if entered_card in ranks_low:
            if input == '5H':
                card_dict['rank'] = rank_dict_low[entered_card]
                output_card = description_rank_dict[entered_card]
                card_dict['description'] = f'a {output_card} of {output_suit}'
            return card_dict
        elif entered_card in ranks_high:
            if input == 'KS':
                card_dict['rank'] = rank_dict_high[entered_card]
                output_card = card_dict['rank']
                card_dict['description'] = f'a {output_card} of {output_suit}'
            return card_dict
        
        else:
            raise ValueError('Sorry mate, thats not a known rank in a deck')
    
    elif len(input) == 3:
        slice_input = input[:2]
        ranks_low = list(rank_dict_low.keys())

        if slice_input in ranks_low:
            if input == '10C':
                entered_suit = input[2:]
                entered_card = input[0:2]
                number_to_word = list(description_rank_dict.keys())
                card_dict['rank'] = rank_dict_low[entered_card]
                card_dict['suit'] = suit_dict[entered_suit]
                output_card = description_rank_dict[entered_card]
                output_suit = card_dict['suit']
                card_dict['description'] = f'a {output_card} of {output_suit}'
                return card_dict   
        else:
            raise ValueError('Sorry mate, thats not a known rank in a deck') 
    


