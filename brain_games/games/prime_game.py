from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def get_question_correct_answer():  # generate of a question to the user
    random_number = randint(1, 50)
    if is_number_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'Question: {random_number}'
    return question, correct_answer
