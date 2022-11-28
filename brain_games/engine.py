import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    for i in range(3):
        question, correct_answer = game.get_question_correct_answer()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '\
{correct_answer}'. Let's try again, {name}!")
        else:
            print('Correct!')
            i += 1
    print(f'Congratulations, {name}!')
