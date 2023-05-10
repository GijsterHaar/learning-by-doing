print()
from pure_palindrome import check_for_invalid_and_clean
from pure_palindrome import check_for_palindrome


def main():
    user_input = input('Please enter a word: ')
    return_check = check_for_invalid_and_clean(user_input)
    if return_check == 'Sorry, that is invalid input':
        print(return_check)
        exit()
    palindrome = check_for_palindrome(return_check)
    print(palindrome)



if __name__ == '__main__':
    main()