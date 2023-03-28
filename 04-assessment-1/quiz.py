import random

def main():
    with open("questions.txt", 'r') as file:
        chunked_file = get_the_file(file)
    quiz_dict = make_quiz_dict(chunked_file)
    count = 0
    correct_score = 0
    welcome()
    check_high_score()
    while count < 5:
        question = get_question(quiz_dict)
        choice = enter_choice()
        correct_score = compare(question, choice, correct_score)
        count += 1
    compare_high_score(correct_score)
    
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

def welcome():
    print('''\nWelcome to my little quiz.
You have to answer 5 questions.\n''')

def check_high_score():
    with open('high_score.txt', 'r') as high_score_file:
        high_score_file = high_score_file.readlines()
        if len(high_score_file) == 0:
            print('There is no high score yet, go ahead and set one\n')
        else:
            print(f'The high score is:\n{high_score_file[0]}\nCan you beat that?\n')

def get_question(quiz_dict):
    question = random.choice(quiz_dict)
    print(question.get('questions'), '\n')
    options = 0
    # answers = question.get('answers')         This is my first code
    # random.shuffle(answers)
    # for pos in answers
    random.shuffle(question['answers'])         # got this from Carla
    for pos in question['answers']:             # got this from Carla
        options += 1
        print(options, pos)
    return question

def enter_choice():
    choice =  int(input("Please enter your choice: "))
    return choice

def compare(question, choice, correct):
    answer = question.get('answers')[choice-1]
    if  answer == question.get('correct'):
        print(f'\nYes, {answer} is the correct answer\n')
        correct += 1
    else:
        print(f'\nNope, {answer} is not correct\n')
    return correct

def write_high_score(correct, high_score):
    print(f'Congratulations, {correct} is the high_score')
    name = input('You may enter your name here: ')
    high_score.write(f'Name: {name}  -  High score: {correct}')

def overwrite_high_score(correct, list_high_score, high_score):
    for score in list_high_score:
        score.split(' ')
        if correct >= int(score[-1]):
            print(f'Congratulations, {correct} is the high_score')
            name = input('You may enter your name here: ')
            high_score.seek(0)
            high_score.truncate()
            high_score.write(f'Name: {name}  -  High score: {correct}')

def compare_high_score(correct):
    with open('high_score.txt', 'r+') as high_score:
        list_high_score = high_score.readlines()
        if list_high_score == []:
            write_high_score(correct, high_score)
        else:
            overwrite_high_score(correct, list_high_score, high_score)   

if __name__ == '__main__':
    main()