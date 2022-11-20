import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    return name


# task = 'What is the result of the expression?'
# question = '5 + 6'
# correct_answer = str(11)



def greet(name):
    print(f'Hello, {name}!')
    return name


# greet(welcome_user())
# print(greet(welcome_user()))




def rounds(name, task, question, correct_answer):
    print(task)
    for i in range(3):
        print(question)
        answer = input()
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
    
# rounds(greet(welcome_user()), task, question, correct_answer)