from random import randint


def generate_question_prime():  # generate of a question to the user
    question = randint(1, 50)
    divider = 2
    while question % divider != 0:
        divider += 1
    if divider == question:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
