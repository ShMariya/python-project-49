import math
from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def get_question_correct_answer():  # generate of a question to the user
    random_number1 = randint(1, 50)
    random_number2 = randint(1, 50)
    question_gcd = f'Question: {random_number1} {random_number2}'
    correct_answer_gcd = str(math.gcd(random_number1, random_number2))
    return question_gcd, correct_answer_gcd
