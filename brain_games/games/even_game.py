from random import randint


def generate_question_even():  # generate of a question to the user
    number = randint(1, 100)
    question_even = f'Question: {number}'
    if number % 2 == 0:
        correct_answer_even = 'yes'
    else:
        correct_answer_even = 'no'
    return question_even, correct_answer_even
