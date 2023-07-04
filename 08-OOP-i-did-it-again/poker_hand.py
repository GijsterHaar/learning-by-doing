from poker_user_input import User_Input
from chunk_wins import Chunk

class Hand:
    def __init__(self, user_input):
        self.valid_input = User_Input(user_input)
        self.straight_wins = Chunk()
        self.__rank_dict = {}
        self.__suit_dict = {}
        self.__rank_list = []
        self.__suit_list = []


    def _check_hand(self):

        for card in self.valid_input.input:
            rank = card[:-1]
            if rank not in self.__rank_dict:
                self.__rank_dict[rank] = 0
            self.__rank_dict[rank] += 1
        for card in self.valid_input.input:
            suit = card[-1]
            if suit not in self.__suit_dict:
                self.__suit_dict[suit] = 0
            self.__suit_dict[suit] += 1

        for rank in self.valid_input.input:
            self.__rank_list.append(rank[:-1])
        self.__rank_list.sort()

        for suit in self.__suit_dict:
            self.__suit_list.append(self.__suit_dict[suit])
        self.__suit_list.sort()

        if len(self.__suit_list) == 1:
            if self.__rank_list == self.straight_wins._rank_royal_flush:
                return "Royal flush"

        if len(self.__rank_dict) == 5:
            return "High card"
        elif len(self.__rank_dict) == 4:
            return "One pair"
        elif len(self.__rank_dict) == 3 and 2 in self.__rank_dict.values():
            return "Two pair"
        elif len(self.__rank_dict) == 3 and 3 in self.__rank_dict.values():
            return "Three of a kind"
        elif len(self.__rank_dict) == 2 and 3 in self.__rank_dict.values():
            return "Full house"
        elif len(self.__rank_dict) == 2 and 4 in self.__rank_dict.values():
            return "Four of a kind"

        
# class Other_Hand:
#     def __init__(self, valid_input):
#         self.valid_input = valid_input