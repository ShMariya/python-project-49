from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(number):
    return number % 2 == 0


def generate_question():  # generate of a question to the user
    number = randint(1, 100)
    question_even = f'Question: {number}'
    if is_number_even(number):
        correct_answer_even = 'yes'
    else:
        correct_answer_even = 'no'
    return question_even, correct_answer_even
