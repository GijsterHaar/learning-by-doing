print()
import random
import sys

# generate a random word
# welcome a player with a message to prompt a guess (1 letter) and a line of dots, one for each letter
# compare the guess with the generated word
# if letter in word replace dots with letter
# countdown to zero
# if word is guessed within turns print succes else print to bad

# have to have a list with 6 values, each value a dot

# have to be able to replace the dot on the right index with guessed character 
# and print that out as a string

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
        word_list.append(word.lower())
    answer = random.choice(word_list)
    print(answer)
    return list(answer)

def guess():
    return list(input("Please enter a character: "))

def compare(answer, your_guess):
    print_answer = []
    for i in answer:
        if i in your_guess:
            print_answer.append(i)
        else:
            print_answer.append('.')
    new_answer = ''.join(print_answer)
    
    print(new_answer)





if __name__ == '__main__':
    main()

print()