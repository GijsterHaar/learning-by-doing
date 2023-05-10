print()
from pure_palindrome import check_for_invalid
from pure_palindrome import clean_user_input
from pure_palindrome import check_for_palindrome

def main():
    user_input = input('Please enter a word: ')
    user_input = check_for_invalid(user_input)
    if user_input == 'Sorry, that is invalid input':
        print(user_input)
        exit()
    cleaned_string = clean_user_input(user_input)
    if cleaned_string == 'Sorry, that is invalid input':
        print(cleaned_string)
        exit()
    palindrome = check_for_palindrome(cleaned_string)
    print(palindrome)



if __name__ == '__main__':
    main()