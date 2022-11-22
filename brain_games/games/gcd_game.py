import math
import random
from random import randint


def generate_question_gcd():#generate of a question to the user
    
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    question_gcd = f'Question: {number1} {number2}'
    correct_answer_gcd = str(math.gcd(number1, number2))
    return question_gcd, correct_answer_gcd

