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
        print('Cannot dic=vide by 0!')
    

def randomNumber():
    random_number = randint(1, 100)
    random1 = random_number
    random_num2 = randint(1,100)
    random2 = random_num2

    return random1, random2

def calculation(num1, num2):

    pass

playing = True

while playing:
    op = input('What do you want to do? Choose one operation +,-,*,/: ')
    operators = ['+', '-', '*', '/']
    while op not in operators:
        print('Invalid option, please choose from one of the options +,-,*,/ ')
        op = input('What do you want to do? Choose one operation +,-,*,/: ')

    if op == '+':



    

