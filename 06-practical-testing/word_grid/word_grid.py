print()
from pure_word_grid import build_word_grid
from pure_word_grid import check_if_invalid



def main():
    checked_word = True
    while checked_word:
        user_input = input("Please type your word: ")
        checked_word = check_if_invalid(user_input)
        if checked_word:
            print(checked_word)
    word_list = build_word_grid(user_input)
    for word in word_list:
        print(word)
    









if __name__ == '__main__':
    main()