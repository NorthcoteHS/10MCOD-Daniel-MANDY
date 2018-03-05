'''
Program:    magic8.py
Name:       Daniel Mandy
Date:       22/2/2018
desc:       create a random number generator
'''
aa = input('do you want to ask the magic8ball a question?(yes/no) ')

#the while loop  
while aa == 'yes':
    # asks user a question
    question = input('Ask the Magic 8 Ball a question, ')

    #makes x = random number
    from random import randint
    x = randint(1, 6)

    #all the different ouputs + linking back to the while loop
    if x == 1:
        print('definatly')
        aa = input('do you want to ask the magic8ball another question?(yes/no) ')
    if x == 2:
        print('maybe')
        aa = input('do you want to ask the magic8ball another question?(yes/no) ')
    if x == 3:
        print('only the future can tell!')
        aa = input('do you want to ask the magic8ball another question?(yes/no) ')
    if x == 4:
        print('yes')
        aa = input('do you want to ask the magic8ball another question?(yes/no) ')
    if x == 5:
        print('no')
        aa = input('do you want to ask the magic8ball another question?(yes/no) ')
    if x == 6:
        print('certainly not')
        aa = input('do you want to ask the magic8ball another question?(yes/no) ')
