print()
import random
import sys

# generate a random word
# welcome a player with a message to prompt a guess (1 letter) and a line of dots, one for each letter
# compare the guess with the generated word
# if letter in word replace dots with letter
# countdown to zero
# if word is guessed within turns print succes else print to bad

def main():
    answer = get_a_word()
    welcome()
    your_guess = guess()
    compare(answer, your_guess)

def welcome():
    print("Welcome to my 6-letter-word hangman game.\nYou have six guesses")
    print()

def get_a_word():
    word_list = []
    word_file = open("6_letter_words.txt")
    for word in word_file:
        word_list.append(word.strip())
    answer = random.choice(word_list)
    print(answer)
    return answer.lower()

def guess():
    return input("Please enter a character: ")

def compare(answer, your_guess):
    for char in answer:
        if char == your_guess:
    
            print(answer.index(your_guess))







if __name__ == '__main__':
    main()

print()