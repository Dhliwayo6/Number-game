from random import *

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else: 
        print('Cannot divide by 0!')
    
def numbers():
    num1 = randint(1,10)
    num2 = randint(1,10)

    return num1, num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print('Welcome to a number game! Let\'s put your math skills to the test!')
print(' ')

player_name = input('What is your name? ').upper()

op = input(f'What do you want to do {player_name}? Choose one operation +,-,*,/: ')
operators = ['+', '-', '*', '/']
while op not in operators:
    print('Invalid option, please choose from one of the options +,-,*,/ ')
    op = input('What do you want to do? Choose one operation +,-,*,/: ')
score = 0   
if op in operations:
    for _ in range(5):
        num1, num2 = numbers()
        result = operations[op](num1, num2)
        x = round(result, 3)
        result = x
        reply = input(f'Calculate {num1} {op} {num2} = ')

        try:
            answer = float(reply)
            if answer == result:
                print('Correct')
                score += 1
            else: 
                print(f'Incorrect, the answer was {result}')
        except ValueError:
            print('That was not a number, try again')
    if score > 3:
        print(f'{player_name} you got {score} questions correct, you did great!')
    else:
        print(f'{player_name} you got {score} questions correct, you can do better!')

    print(f'You got {((score/5) * 100)} %')



         
        

    