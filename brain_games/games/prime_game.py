from random import randint


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def generate_question():  # generate of a question to the user
    number = randint(1, 50)
    if is_number_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'Question: {number}'
    return question, correct_answer
