print()

from pure_new_number import check_for_valid_input
from pure_new_number import get_magic_number
from pure_new_number import check_winning
from pure_new_number import get_end_message

def main():
    magic_number = get_magic_number()
    print('Welcome to my number guessing name.\nYou have six guesses.\n')
    guesses = 6
    wrong_guess = True
    play_game = True
    while wrong_guess and play_game and guesses > 0:
        user_guess = input('Enter any number between 1 and 100: ')
        wrong_guess = check_for_valid_input(user_guess)
        if wrong_guess:
        
            play_game = check_winning(user_guess, magic_number)
            if play_game == False:
                print(f'\nYes, {user_guess} is the magic number\n')
            elif play_game == 'To low': 
                print(f'\nSorry, {user_guess} is to low\n')
                guesses -= 1
            else:
                play_game == "To high"
                print(f'\nSorry, {user_guess} is to high\n')
                guesses -= 1
    if guesses == 0:
        end_message = get_end_message(user_guess, magic_number)
        if end_message:
            print(f'\nYes, {user_guess} is the magic number\n')
        else:
            print(f'{magic_number} is the magic number\n')










if __name__ == '__main__':
    main()