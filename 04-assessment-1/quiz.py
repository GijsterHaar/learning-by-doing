import random
import file_handling

def main():
    quiz_dict = file_handling.main()
    count = 0
    correct = 0
    check_high_score()
    while count < 5:
        question = get_question(quiz_dict)
        choice = enter_choice()
        correct = compare(question, choice, correct)
        count += 1
    file_handling.compare_high_score(correct)
    

def check_high_score():
        high_score_file = file_handling.high_score_data()
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
        correct += 1
        print(f'\nYes, {answer} is the correct answer\nYour score is {correct}\n')
    else:
        print(f'\nNope, {answer} is not correct\n')
    return correct



if __name__ == '__main__':
    main()