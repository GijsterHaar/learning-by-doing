
def parse_card(input):

    suit_dict = {'C': 'clubs', 'D': 'diamonds', 'H': 'hearts', 'S': 'spades'}
    rank_dict = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
                  '9': '9', '10': '10', 'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'}
    description_rank_dict = {'2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six','7': 'seven',
                             '8': 'eight', '9': 'nine', '10': 'ten','J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'}
    card_dict = {}
    AN = ['8', 'A']

    if type(input) != str or len(input) <1:
        raise ValueError('Sorry mate, wrong input means no output')
    
    elif input == input.lower():
        raise ValueError('This is no valid choice, use capital')
    
    elif len(input) < 2 or len(input )> 3:
        raise ValueError('You did not enter the correct amount of characters')
    
    if len(input) == 2:
        entered_suit = input[1:]
        entered_card = input[0:1]
        if entered_suit not in list(suit_dict.keys()):
            raise ValueError('Sorry mate, thats not a known suit in a deck')
        elif entered_card not in list(rank_dict.keys()):
            raise ValueError('Sorry mate, thats not a known rank in a deck')
        elif entered_suit in suit_dict and entered_card in rank_dict:
            card_dict = parse_input(card_dict, suit_dict, rank_dict, description_rank_dict, entered_suit, entered_card)
            if entered_card in AN:
                card_dict['description'] = f'an {description_rank_dict[entered_card]} of {suit_dict[entered_suit]}'
        return card_dict

    if len(input) == 3:
        entered_suit = input[2:]
        entered_card = input[:2]
        if entered_card == '10':
            card_dict = parse_input(card_dict, suit_dict, rank_dict, description_rank_dict, entered_suit, entered_card)
            return card_dict
        else:
            raise ValueError('Sorry mate, with no 10 involved three characters is a wrong input')
    
def parse_input(card_dict, suit_dict, rank_dict, description_rank_dict, entered_suit, entered_card):
    card_dict['suit'] = suit_dict[entered_suit]
    card_dict['rank'] = rank_dict[entered_card]
    output_suit = card_dict['suit']
    card_dict['description'] = f'a {description_rank_dict[entered_card]} of {output_suit}'
    return card_dict
