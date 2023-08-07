from hand import Hand

def main():

    hand_player_1 = input("\nPlayer one, please enter a poker hand: ")
    hand_player_2 = input("Player two, please enter a poker hand: ")
    player_1 = Hand(hand_player_1)
    player_2 = Hand(hand_player_2)
    compare(player_1, player_2)


def compare(player_1, player_2):
    if player_1 == player_2:
        max_count_card_player_1 = max(len(val) for val in player_1.ordered_dict.values())
        max_key_player_1 = [key for key, val in player_1.ordered_dict.items() if len(val) == max_count_card_player_1]
        max_count_card_player_2 = max(len(val) for val in player_2.ordered_dict.values())
        max_key_player_2 = [key for key, val in player_2.ordered_dict.items() if len(val) == max_count_card_player_2]

        if max_key_player_1 < max_key_player_2:
            print(f'\nYou both have a {str(player_1)}\nBut player two wins with a higher rank\n')
        elif max_key_player_2 < max_key_player_1:
            print(f'\nYou both have a {str(player_1)}\nBut player one wins with a higher rank\n')


    if player_1 < player_2:
        print(f'Player one, you have a {str(player_1)}')
        print(f'Player two wins with a {str(player_2)}')
    elif player_2 < player_1:
        print(f'Player two, you have a {str(player_2)}')
        print(f'Player one wins with a {str(player_1)}')



if __name__ == '__main__':
    main()