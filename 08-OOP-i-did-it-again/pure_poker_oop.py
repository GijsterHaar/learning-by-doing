"""
chunked and ordered lists with possible winning ranks and possible winning suits

store input
class User_Input:
    class atr: empty list  
    method: filter out invalid
    method: split the user input in a user input list
    method: append every item in user input list to empty list (to separate what we work with from the user input)

class Hand:
    class atr: count_ranks
    class atr: count_suits
    method: split the list entries in ranks and suits


class compare_input_to_possible_wins:
    method: return str

make 2 instances for each hand
compare values of instances

"""


class User_Input:   # here I make sure we get a good input hand and create a separate list of cards
    def __init__(self, user_input):
        self.input = user_input
    
    def check_invalid(self):
        if not isinstance(self.input, str) or len(self.input.split()) != 5:
            return "Sorry, that's invalid input"
        for char in self.input:
            if not char.isalnum():
                return "Sorry, that's invalid input"
    
    def split_input(self):
        self.__input_list = []
        for i in self.input.split():
            self.__input_list.append(i)
        return self.__input_list
    


class Hand(User_Input):  # here I will separate the ranks from the suits and count
    def __init__(self, user_input):
        User_Input.__init__(self, user_input)
        self.__rank_dict = {}
        self.__suit_dict = {}
    
    def count_ranks(self):
        for i in self.split_input():
            rank = i[:-1]
            if rank not in self.__rank_dict:
                self.__rank_dict[rank] = 0
            self.__rank_dict[rank] += 1
        return self.__rank_dict
    
    def count_suits(self):
        for i in self.split_input():
            suit = i[-1]
            if suit not in self.__suit_dict:
                self.__suit_dict[suit] = 0
            self.__suit_dict[suit] += 1
        return self.__suit_dict

    



    


