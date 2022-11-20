import prompt
import random
from random import randint

def welcome_user():
    name = prompt.string('May I have your name? ')
    return name


def greet(name):
    print(f'Hello, {name}!')
    return name


def generate_question():
    pass

def rounds(name, task, question_correct_answer):
    print(task)
    for i in range(3):
        question, correct_answer = question_correct_answer
        print(question)
        answer = input()
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'. \
Let's try again, {name}!")
            break

        else:
            print('Correct!')
            i += 1
        if i == 3:
            print(f'Congratulations, {name}!')
