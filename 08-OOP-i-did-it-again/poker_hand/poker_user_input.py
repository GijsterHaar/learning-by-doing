"""
chunked and ordered lists with possible winning ranks and possible winning suits

store input
class User_Input:
    V class atr: empty list 
    V method: filter out invalid
    V method: split the user input in a user input list 
    V method: append every item in user input list to empty list (to separate what we work with from the user input)

class Hand:
    cV lass atr: count_ranks
    V class atr: count_suits
    V method: split the list entries in ranks and suits


class compare_input_to_possible_wins:
    method: return str

make 2 instances for each hand
compare values of instances

"""

legal_char = ['2','3','4','5','6','7','8','9','10',
               'J','Q','K','A', 'H', 'C', 'D', 'S', ' ']

class User_Input:
    def __init__(self, user_input):
        self.input = user_input
        self.check_invalid()
        self.input = self.input.split()
        
    
    def check_invalid(self):
        if not isinstance(self.input, str) or self.input == "" \
            or len(self.input.split()) != 5:
            raise TypeError("Your input is invalid")

        for card in self.input.split():
            for char in card:
                if not char.isalnum():
                    raise TypeError("Your input is invalid")
            if card[:-1] not in legal_char or card[-1] not in legal_char:
                raise TypeError("Your input is invalid")
        