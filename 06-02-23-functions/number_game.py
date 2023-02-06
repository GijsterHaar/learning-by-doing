print()

# need to generate a random number between 1 and 100
# need an input
# need conditionals to check
# need to print "wrong" of "guessed it"

from random import randint


def main():
    generate_number()
    enter_guess()
    compare()


def generate_number():
    global answer
    answer = randint(1, 101)


def enter_guess():
    global guess
    guess = int(input("Please enter your guess here: "))


def wrong_answer():
        if guess < answer:
            print(f"{guess} is to low, try again")
        elif guess > answer:
            print(f"{guess} is to high, try again")


def compare():
    while guess != answer:
        wrong_answer()
        enter_guess()
    print(f"You did good, the answer is {answer}")


if __name__ == '__main__':
    main()



print()