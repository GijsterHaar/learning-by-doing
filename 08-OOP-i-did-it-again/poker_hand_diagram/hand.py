from card import Card
from typing import Any
from rank import Rank


class Hand:
    def __init__(self, hand: object) -> None:
        self.hand = self._check_invalid(hand)
        self.cards = sorted([Card(card) for card in self.hand]) # got this from Carla
        self.ordered_list = self.order_my_cards()
    
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
    
    def order_my_cards(self) -> dict[str, list[str]]: # Got this from Carla
        ordered_dict = {}
        for card in self.cards:
            if card.valid_rank not in ordered_dict:
                ordered_dict[card.valid_rank] = []
            ordered_dict[card.valid_rank].append(card)
        return ordered_dict # {'10': ['10D'], '2': ['2H'], '5': ['5H'], '7': ['7H'], '8': ['8H']}
    
    def name_the_hand(self) -> str:  # {'10': ['10D'], '2': ['2H'], '5': ['5C', '5H'], '7': ['7H']}
        if len(self.ordered_list) == 4:
            return 'One Pair'
        elif len(self.ordered_list) == 3:
            for value in self.ordered_list.values():
                if len(value) == 2 or len(value) == 1:
                    return 'Two Pair'
                return 'Three of a Kind'
        elif len(self.ordered_list) == 2:
             for value in self.ordered_list.values():
                if len(value) == 3 or len(value) == 2:
                    return 'Full House'
                return 'Four of a Kind'
        return 'High Card'
