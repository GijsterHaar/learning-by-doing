print()

from pure_new_number import check_for_valid_input
from pure_new_number import get_magic_number
from pure_new_number import check_guess
from pure_new_number import check_end_message
from pure_new_number import get_end_message
from pure_new_number import get_guess_result

def main():
    magic_number = get_magic_number()
    print('Welcome to my number guessing name.\nYou have six guesses.\n')
    turns = 6
    guesses = True
    play_game = True
    

    while guesses and play_game and turns > 0:
        user_guess = input('Enter any number between 1 and 100: ')
        guesses = check_for_valid_input(user_guess)
        if guesses:
            play_game = check_guess(user_guess, magic_number)
            message, turns = get_guess_result(play_game, user_guess, turns)
            print(message)

    if turns == 0:
        end_message = check_end_message(user_guess, magic_number)
        end_message = get_end_message(end_message, user_guess, magic_number)
        print(end_message)



if __name__ == '__main__':
    main()