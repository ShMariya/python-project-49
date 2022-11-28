import random
from random import randint


TASK = 'What number is missing in the progression?'


def get_progression():
    first_member = randint(1, 5)
    step = randint(1, 5)
    progression = [first_member]
    for i in range(10):
        progression.append(first_member + step * (i + 1))
        i += 1
    return progression


def get_question_correct_answer():  # generate of a question to the user
    progression = get_progression()
    correct_answer = random.choice(progression)
    progression[progression.index(correct_answer)] = '..'
    question = 'Question: '
    for i in progression:
        question += str(i) + ' '
    return question.strip(), str(correct_answer)
