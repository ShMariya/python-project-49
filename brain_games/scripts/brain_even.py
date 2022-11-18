#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user


def is_even():

    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = input()
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

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
    is_even()


if __name__ == '__main__':
    main()
