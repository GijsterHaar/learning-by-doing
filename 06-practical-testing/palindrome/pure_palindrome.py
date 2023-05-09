print()

def check_for_invalid(user_input):
    if user_input == '' or not isinstance(user_input, str):
        return 'Sorry, that is invalid input'
    else:
        return user_input

def clean_user_input(user_input):
    user_input_list = [i for i in user_input if i.isalnum()]
    user_input = "".join(user_input_list)
    return user_input.lower()

def check_for_palindrome(cleaned_string):
    if cleaned_string[:] != cleaned_string [::-1]:
        return 'Not a palindrome'
    return 'Yes, this is a palindrome'