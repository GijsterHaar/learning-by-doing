print()
import random

def main():
    word = get_a_word()
    count = 6
    answer_line = ['.', '.', '.', '.', '.', '.']
    welcome()
    your_guess = guess()
    first_compare(word, your_guess, answer_line, count)

def get_a_word():
    word_list = []
    word_file = open("hangman_words.txt")
    for words in word_file:
        word_list.append(words.strip().lower())
    word = random.choice(word_list)
    print(word)
    return list(word)

def welcome():
    print("Welcome to my 6-letter-word hangman game.\nYou have six guesses.\n......")
    print()

def guess():
    return input("Please enter a character: ")

def first_compare(word, your_guess, answer_line, count):
    for i, char in enumerate(word):
        if your_guess == char:
            answer_line.pop(i)
            answer_line.insert(i, your_guess)
    first_print_and_into_the_loop(word, answer_line, count)

def first_print_and_into_the_loop(word, answer_line, count):
    while answer_line != word and count > 1:
        answer_line = ''.join(answer_line)
        print(answer_line)
        count, word, answer_line = and_loop_again(count, word, answer_line)
    stop(word, answer_line)

def and_loop_again(count, word, answer_line):
    count -= 1
    your_guess = guess()
    answer_line = list(answer_line)
    check_looping(word, answer_line, your_guess)
    return count, word, answer_line

def check_looping(word, answer_line, your_guess):
    for i, char in enumerate(word):
        if your_guess == char:
            answer_line.pop(i)
            answer_line.insert(i, your_guess)
    return word, answer_line, your_guess
    

def stop(word, answer_line):
    if word == answer_line:
        answer_line = ''.join(answer_line)
        print(f'Yes, you did it, {answer_line} is the correct answer')
    else:
        word = ''.join(word)
        print(f"Sorry mate, you'r hanging, {word} is the correct word")

if __name__ == '__main__':
    main()

print()