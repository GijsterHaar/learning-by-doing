print()

from random import randint

def get_magic_number():
    magic_number = randint(1, 100)
    return magic_number

def check_for_valid_input(user_guess):
    try:
        user_guess = int(user_guess)
    except:
        return 'Invalid input'
    if int(user_guess) < 1 or int(user_guess) > 100:
        return 'Invalid input'
    return True

def check_guess(user_guess, magic_number):

    if int(user_guess) == magic_number:
        return False
    elif int(user_guess) < magic_number:
        return "To low"
    else:
        return "To high"

def get_guess_result(play_game, user_guess, turns):
    if play_game == False:
        message = f'\nYes, {user_guess} is the magic number\n'
    elif play_game == 'To low':
        message = f'\nSorry, {user_guess} is to low\n'
        turns -= 1
    else:
        play_game == "To high"
        message = f'\nSorry, {user_guess} is to high\n'
        turns -= 1
    return message, turns


def get_end_message( magic_number):
    end_message =f'{magic_number} is the magic number\n'
    return end_message
    
   


    
    
