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

def check_winning(user_guess, magic_number):

    if int(user_guess) == magic_number:
        return False
    elif int(user_guess) < magic_number:
        return "To low"
    else:
        return "To high"

def get_end_message(user_guess, magic_number):
    if user_guess == magic_number:
        return True
    return False
    
    
   


    
    
