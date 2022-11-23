import random
from random import randint


def generate_question_progress():  # generate of a question to the user
    first_member = randint(1, 5)
    step = randint(1, 5)
    progression = [first_member]
    for i in range(10):
        progression.append(first_member + step * (i + 1))
        i += 1
    correct_answer = random.choice(progression)
    progression[progression.index(correct_answer)] = '..'
    question = ''
    for i in progression:
        question += str(i) + ' '
    return question.strip(), str(correct_answer)
