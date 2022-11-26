import prompt


def star_game(game):
    print('Welcome to the Brain Games!\nMay I have your name?', end=' ')
    name = input()
    print(f'Hello, {name}!\n{game.task}')
    for i in range(3):
        question, correct_answer = game.generate_question()
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
