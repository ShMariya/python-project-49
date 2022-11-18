#!/usr/bin/env python3
import random
from random import randint
from brain_games.cli import welcome_user


def calc():

    name = welcome_user()

    print('What is the result of the expression?.')
    for i in range(3):
        number1 = randint(1, 50)
        number2 = randint(1, 50)
        operators = ['+', '-', '*']
        operator = random.choice(operators)
        print(f'Question: {number1} {operator} {number2}')
        answer = int(input())
        if operator == '+':
            correct_answer = number1 + number2
        if operator == '-':
            correct_answer = number1 - number2
        if operator == '*':
            correct_answer = number1 * number2

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\
Let's try again, {name}!")
            break

        else:
            print('Correct!')
            i += 1
        if i == 3:
            print(f'Congratulations, {name}!')


def main():
    calc()


if __name__ == '__main__':
    main()
