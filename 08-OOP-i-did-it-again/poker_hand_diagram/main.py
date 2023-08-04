from hand import Hand

"""
I need to create 2 players. Will do that making 2 instances of class Hand
and pass a poker hand that comes from an input function

Now I should be able to perform all class methods on those instances



"""

def main():

    hand_player_1 = input("Player one, please enter a poker hand: ")
    hand_player_2 = input("Player two, please enter a poker hand: ")
    player_1 = Hand(hand_player_1)
    player_2 = Hand(hand_player_2)
    compare(player_1, player_2)


def compare(player_1, player_2):
    if player_1 == player_2:
        print(f'You both have a {str(player_1)}')
        # here comes the code to compare equal hand by using the highest rank


    if player_1 < player_2:
        print(f'Player one, you have a {str(player_1)}')
        print(f'Player two wins with a {str(player_2)}')
    else:
        print(f'Player two, you have a {str(player_2)}')
        print(f'Player one wins with a {str(player_1)}')


    # print(player_1)
    # print(player_2)


if __name__ == '__main__':
    main()