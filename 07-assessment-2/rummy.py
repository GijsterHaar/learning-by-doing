from pure_rummy import description_rummy_hand

def main():
    user_input = input("What's your hand? ")
    rummy_hand = description_rummy_hand(user_input)
    print(rummy_hand)



if __name__ == '__main__':
    main()