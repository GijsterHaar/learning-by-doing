print()
from pure_poker import description_poker_hand

def main():
    user_data = input("What's your hand? ")
    things_to_print = description_poker_hand(user_data)
    print(things_to_print)





if __name__ == '__main__':
    main()
