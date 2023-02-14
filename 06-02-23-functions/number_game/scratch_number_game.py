print()

from random import randint

def main():
    count = 6
    welcome()
    target_number = get_random_number()
    compare_numbers(target_number, count)

def welcome():
    print("Welcome to my number guessing name.\nYou have six guesses.") 
    print()

def get_random_number():
    return randint(1, 100)

def enter_guess():
    return int(input("Please enter a number: "))

def wrong_number(target_number, your_guess):
    if your_guess < target_number:
        print(f"{your_guess} is too low, try again")
    elif your_guess > target_number:
        print(f"{your_guess} is too high, try again")

def stop(target_number, your_guess):
    if target_number != your_guess:
        print(f"Sorry, also {your_guess} is incorrect.\nAnd six guesses is the max.")
    else:
        print(f"You did it, {your_guess} is the correct answer")

def compare_numbers(target_number, count):
    your_guess = enter_guess()
    if target_number != your_guess:
        while count > 1:
            wrong_number(target_number, your_guess)
            count -= 1
            print(f"You have {count} tries left")
            your_guess = enter_guess()
    stop(target_number, your_guess)


if __name__ == '__main__':
    main()