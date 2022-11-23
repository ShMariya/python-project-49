from random import randint


def generate_question_prime():  # generate of a question to the user
    number = randint(1, 50)
    divider = 2
    while number % divider != 0:
        divider += 1
    if divider == number:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'Question: {number}'
    return question, correct_answer
