from card import Card
from typing import Any, Dict, List
from rank import Rank


class Hand:
    def __init__(self, hand: object) -> None:
        self.hand = self._check_invalid(hand)
        self.cards = sorted([Card(card) for card in self.hand]) # got this from Carla
        self.ordered_dict = self._order_my_cards()
    
    def _check_invalid(self, hand: object) -> list[str]:
        if not isinstance(hand, str):
            raise TypeError("Your input is invalid")
        cards_list = sorted(hand.split())
        if not len(cards_list) == 5:
            raise ValueError("That's not the right amount of cards in a hand")
        for card in cards_list:
            Card(card)  # check if every card in the hand has valid rank and suit
        for i in range(len(cards_list)-1):
            if cards_list[i] == cards_list[i+1]:
                raise ValueError("There are duplicate cards in your hand")
        return cards_list
    
    def _order_my_cards(self) -> Dict[str, List[str]]: # Got this from Carla
        ordered_dict: Dict[Any, Any] = {}
        for card in self.cards:
            if card.valid_rank not in ordered_dict:
                ordered_dict[card.valid_rank] = []
            ordered_dict[card.valid_rank].append(card)
        return ordered_dict # {'10': ['10D'], '2': ['2H'], '5': ['5H'], '7': ['7H'], '8': ['8H']}
    

    def _name_the_hand(self) -> str:

        checks = ((check_for_four_of_a_kind, 'Four Of A Kind'),
                (check_for_full_house, 'Full House'),
                (check_for_two_pair, 'Two Pair'),
                (check_for_three_of_a_kind, 'Three Of A Kind'),
                (check_for_one_pair, 'One Pair'),
                (check_for_high_card, 'High Card'))

        for check_function, value in checks:
            if check_function(self):
                return_card = value
                break
        return return_card


def check_for_one_pair(self: Any) -> bool:
    return len(self.ordered_dict) == 4

def check_for_two_pair(self: Any) -> bool:
    return len(self.ordered_dict) == 3 and any([len(value) == 2 for value in self.ordered_dict.values()])

def check_for_three_of_a_kind(self: Any) -> bool:
    return len(self.ordered_dict) == 3 and any([len(value) == 3 for value in self.ordered_dict.values()])

def check_for_full_house(self: Any) -> bool:
    return len(self.ordered_dict) == 2 and any([len(value) == 2 for value in self.ordered_dict.values()])

def check_for_four_of_a_kind(self: Any) -> bool:
    return len(self.ordered_dict) == 2 and any([len(value) == 1 for value in self.ordered_dict.values()])

def check_for_high_card(self: Any) -> bool:
    return True
