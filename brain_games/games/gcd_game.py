import math
from random import randint


task = 'Find the greatest common divisor of given numbers.'


def generate_question():  # generate of a question to the user
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    question_gcd = f'Question: {number1} {number2}'
    correct_answer_gcd = str(math.gcd(number1, number2))
    return question_gcd, correct_answer_gcd
