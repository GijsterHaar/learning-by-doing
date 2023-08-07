from card import Card
from typing import Dict, List
from rank import Rank
from suit import Suit
from chunk_seq_of_ranks import Chunk


class Hand:
    def __init__(self, hand: object) -> None:
        self.hand = self._check_invalid(hand)
        self.cards = sorted([Card(card) for card in self.hand]) # got this from Carla
        self.ordered_dict = self._order_my_cards()
        self.count_suits =  self._count_my_suits()
        self.chunks = Chunk()
        self.seq = [key.rank for key in self.ordered_dict]
        self.seq.sort()
        self.return_card = self._name_the_hand()
    

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
    

    def _order_my_cards(self) -> Dict[Rank, List[Card]]: # Got this from Carla
        ordered_dict: Dict[Rank, List[Card]]= {}
        for card in self.cards:
            if card.valid_rank not in ordered_dict:
                ordered_dict[card.valid_rank] = []
            ordered_dict[card.valid_rank].append(card)
        return ordered_dict # {'10': ['10D'], '2': ['2H'], '5': ['5H'], '7': ['7H'], '8': ['8H']}
    

    def _count_my_suits(self) -> List[Suit]:
        suit_count = []
        suit_count = [suit_count.append(card.valid_suit) for card in self.cards if card.valid_suit not in suit_count]
        return suit_count
    

    def _name_the_hand(self) -> tuple[str,int]:

        checks = ((self._check_royal_flush, 'Royal Flush', 10),
                (self._check_straight_flush, 'Straight Flush', 9),
                (self._check_flush, 'Flush', 8),
                (self._check_straight, 'Straight', 7),
                (self._check_four_of_a_kind, 'Four Of A Kind', 6),
                (self._check_full_house, 'Full House', 5),
                (self._check_three_of_a_kind, 'Three Of A Kind', 4),
                (self._check_two_pair, 'Two Pair', 3),
                (self._check_one_pair, 'One Pair', 2),
                (self._check_high_card, 'High Card', 1))

        for check_function, value, score in checks:
            if check_function():
                return_card = value, score
                break
        return return_card

   
    def _check_royal_flush(self) -> bool:
        return len(self.count_suits) == 1 and self.seq == self.chunks._ranks_royal_flush

    def _check_straight_flush(self) -> bool:
        return len(self.count_suits) == 1 and self.seq in self.chunks._ranks_straight_flush

    def _check_flush(self) -> bool:
        return len(self.count_suits) == 1
    
    def _check_straight(self) -> bool:
        return len(self.ordered_dict) == 5 and self.seq in self.chunks._ranks_straight
    
    def _check_four_of_a_kind(self) -> bool:
        return len(self.ordered_dict) == 2 and any([len(value) == 1 for value in self.ordered_dict.values()])

    def _check_full_house(self) -> bool:
        return len(self.ordered_dict) == 2 and any([len(value) == 2 for value in self.ordered_dict.values()])

    def _check_three_of_a_kind(self) -> bool:
        return len(self.ordered_dict) == 3 and any([len(value) == 3 for value in self.ordered_dict.values()])

    def _check_two_pair(self) -> bool:
        return len(self.ordered_dict) == 3 and any([len(value) == 2 for value in self.ordered_dict.values()])

    def _check_one_pair(self) -> bool:
        return len(self.ordered_dict) == 4

    def _check_high_card(self) -> bool:
        return True
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Hand):
            return self.return_card[-1] == other.return_card[-1]
    
    def __gt__(self, other: object) -> bool:
        if isinstance(other, Hand):
            return self.return_card[-1] > other.return_card[-1]
    
    def __lt__(self, other: object) -> bool:
        if isinstance(other, Hand):
            return self.return_card[-1] < other.return_card[-1]
    
    def __str__(self) -> str:
        return self.return_card[0]

