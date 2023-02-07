print()

# need to generate a random number between 1 and 100
# need an input
# need conditionals to check
# need to print "wrong" or "guessed it"

from random import randint

def main():
    target_number = get_random_number()
    your_guess = enter_guess()
    compare_numbers(target_number, your_guess)
 

def get_random_number():
    return randint(1, 101)

def enter_guess():
    return int(input("Please enter a number: "))


def wrong_number(target_number, your_guess):
    if your_guess < target_number:
        print(f"{your_guess} is to low, try again")
    elif your_guess > target_number:
        print(f"{your_guess} is to high, try again")


def compare_numbers(target_number, your_guess):
    for _ in range(6):
        while target_number != your_guess:
            wrong_number(target_number, your_guess)
            your_guess = enter_guess()
        else:
            print("you did it")
    


if __name__ == '__main__':
    main()