print()


def check_if_invalid(word):
    if word is None or not str(word).isalpha():
        return "Sorry, that's invalid"
    return None


def build_word_grid(word):
    word_list = []
    for i in range(len(word)):
        previous_lower = word[:i].lower()
        capital_char = word[i].upper()
        last_lower = word[i+1:].lower()
        word = previous_lower + capital_char + last_lower
        word_list.append(word)
    return word_list   



    