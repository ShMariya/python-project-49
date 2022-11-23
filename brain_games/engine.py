import prompt
# import random
# from random import randint
import brain_games.games.calc_game
import brain_games.games.even_game
import brain_games.games.gcd_game
import brain_games.games.progression_game
import brain_games.games.prime_game



def welcome_user(): #приветствуем и узнаем имя игрока
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name


def greet(name): #здороваемся с игроком
    print(f'Hello, {name}!')
    return name


def rounds(name, task, question_correct_answer, game):
    print(task)
    for i in range(3):
        if game == 'calc':
            question_correct_answer = brain_games.games.calc_game.generate_question_calc()
        elif game == 'even':
            question_correct_answer = brain_games.games.even_game.generate_question_even()
        elif game == 'find_gcd':
            question_correct_answer = brain_games.games.gcd_game.generate_question_gcd()
        elif game == 'progression':
            question_correct_answer = (brain_games.games.progression_game
                                       .generate_question_progress())
        elif game == 'prime':
            question_correct_answer = (brain_games.games.prime_game
                                       .generate_question_prime())
        question, correct_answer = question_correct_answer
        print(question)
        answer = prompt.string('Your answer: ')
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
    rounds(greet(welcome_user()), task,
           brain_games.games.calc_game.generate_question_calc(),
           'calc')
    

def is_even():
    
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    rounds(greet(welcome_user()), task,
           brain_games.games.even_game.generate_question_even(),
           'even')

def find_gcd():
    
    task = 'Find the greatest common divisor of given numbers.'
    rounds(greet(welcome_user()), task,
           brain_games.games.gcd_game.generate_question_gcd(),
           'find_gcd')

def find_missing_number():
    
    task = 'What number is missing in the progression?'
    rounds(greet(welcome_user()), task,
            brain_games.games.progression_game.generate_question_progress(),
            'progression')
    
def is_prime():
    
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    rounds(greet(welcome_user()), task,
           brain_games.games.prime_game.generate_question_prime(),
           'prime')
    