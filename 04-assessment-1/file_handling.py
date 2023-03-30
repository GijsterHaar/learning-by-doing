import quiz


def main():
    with open("questions.txt", 'r') as file:
        chunked_file = get_the_file(file)
    quiz_dict = make_quiz_dict(chunked_file)
    return quiz_dict

def get_the_file(file):
    file = file.readlines()
    clean_file = [i.strip() for i in file]
    chunk_size = 3
    chunked_file = [clean_file[i:i + chunk_size] for i in range(0, len(clean_file), chunk_size)]
    return chunked_file

def make_quiz_dict(chunked_file):
    quiz_dict, key_list = [], ['questions', 'answers', 'correct']
    for entries in chunked_file:
        zip_dict = dict(zip(key_list, entries))
        zip_dict['answers'] = zip_dict['answers'].split(', ')
        quiz_dict.append(zip_dict)
    return quiz_dict

def high_score_data():
    print('''\nWelcome to my little quiz.
    You have to answer 5 questions.\n''')
    with open('high_score.txt', 'r') as high_score_file:
        high_score_file = high_score_file.readlines()
    return high_score_file

def write_high_score(correct, high_score):
    print(f'Congratulations, {correct} is the high_score')
    name = input('You may enter your name here: ')
    high_score.write(f'Name: {name}  -  High score: {correct}')

def overwrite_high_score(correct, list_high_score, high_score):
    for score in list_high_score:
        score.split(' ')
        if correct >= int(score[-1]):
            with open('high_score.txt', 'w+') as high_score:
                print(f'Congratulations, {correct} is the high_score')
                name = input('You may enter your name here: ')
                high_score.write(f'Name: {name}  -  High score: {correct}')

def compare_high_score(correct):
    with open('high_score.txt', 'r+') as high_score:
        list_high_score = high_score.readlines()
        if list_high_score == []:
            write_high_score(correct, high_score)
        else:
            overwrite_high_score(correct, list_high_score, high_score)