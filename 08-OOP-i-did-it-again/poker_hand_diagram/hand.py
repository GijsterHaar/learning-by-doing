from card import Card

class Hand:
    def __init__(self, hand: object) -> None:
        self.hand = self._check_invalid(hand)
    
    def _check_invalid(self, hand: object) -> str:
        if not isinstance(hand, str):
            raise TypeError("Your input is invalid")
        if not len(hand.split(" ")) == 5:
            raise ValueError("That's not the right amount of cards in hand")
        for card in hand.split(" "):
            Card(card)  # check if every card in the hand has valid rank and suit
        return hand

