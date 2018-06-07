'''
Prog:       Study Budy CAT 2.py
Name:       Daniel Mandy
Date:       2018/05/08
Desc:       gives you a maths problem and tells you weather your answer is correct.
'''

#allows the program to repeat after every solve
keepgoing = 'yes'

#allows everything to be much neater later on in the coding
def thisq():
    print('You chose this question')
    
#intro message 
print('This is a program designed to help you with addition')

while keepgoing == 'yes':
    
    #lets you choose difficulty
    #difficulty = input('Please enter a difficulty.(easy): ')
    difficulty = 'easy'
    if difficulty  == 'easy':
    
        #creates all the variables in the above question
        from random import randint
        a = randint(10, 99)
    
        from random import randint
        b = randint(10, 99)
    
        from random import randint
        c = randint(100, 999)
    
        #creates a list of easy questions to choose from
        easyqs = [str(a) + '+' + str(b), str(a) + '+' + str(c), str(c) + '+' + str(b)]
        
        #lists all the questions
        for i,item in enumerate(easyqs):
            print('Question #', i)
            print(item)
        
        #lets you choose what question you want
        print('')
        choice = int(input('please choose a question by typing the number above it: '))
        
        #shows you the question you chose
        if choice == 0:
            thisq()
            print(str(a) + '+' + str(b))
            
        if choice == 1:
            thisq()
            print(str(a) + '+' + str(c))
            
        if choice == 2:
            thisq()
            print(str(c) + '+' + str(b))
        
        #asks the user to input the answer to their question of choice
        print('')
        answer = int(input('Please Enter an Answer: '))
        if choice == 0:
            if answer == (a+b):
                print('Corect!')
                print('')
            else:
                print('incorrect!')
                print('')
                
        if choice == 1:
            if answer == (a+c):
                print('Corect!')
                print('')
            else:
                print('incorrect!')
                print('')
        
        if choice == 2:
            if answer == (c+b):
                print('Corect!')
                print('')
            else:
                print('incorrect!')
                print('')
                
                