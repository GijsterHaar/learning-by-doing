print()
from pure_poker import description_poker_hand

def main():
    user_data = input("What's your hand? ")
    card_hand = description_poker_hand(user_data)
    print(card_hand)





if __name__ == '__main__':
    main()


