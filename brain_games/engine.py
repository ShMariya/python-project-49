import prompt
import random
from random import randint
import brain_games.games.calc_game
import brain_games.games.even_game


def welcome_user(): #узнаем имя игрока
    name = prompt.string('May I have your name? ')
    return name


def greet(name): #приветствие игрока
    print(f'Hello, {name}!')
    return name


def rounds(name, task, question_correct_answer, game):
    print(task)
    for i in range(3):
        if game == 'calc':
            question_correct_answer = brain_games.games.calc_game.generate_question_calc()
        elif game == 'even':
            question_correct_answer = brain_games.games.even_game.generate_question_even()
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


def calc():
    
    task = 'What is the result of the expression?'
    # question, correct_answer = generate_question()
    rounds(greet(welcome_user()), task, brain_games.games.calc_game.generate_question_calc(), 'calc')
    

def is_even():
    
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    # question, correct_answer = generate_question()
    rounds(greet(welcome_user()), task, brain_games.games.even_game.generate_question_even(), 'even')
