'''
prog:       functions testing.py
name:       Daniel Mandy
date:       2018/05/03
desc:       practice using functions
'''

#prints hooray
def hooray():
    print('Hooray!')
    
hooray()

#subtracts 1 number from another
def subtract(x,y):
    return(x - y)

z = subtract(6,2)
print(z)

#takes a number and doubles it
def double(x):
    return(x*2)

#z = int(input('Enter a Number: '))
z = int(input('Enter a Number: '))
z = int(z)
z = double(z)
print(z)


