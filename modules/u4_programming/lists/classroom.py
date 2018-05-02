'''
prog:       classroom.py
name:       Daniel Mandy
date:       2018/05/02
desc:       practice creating and fiddling with lists
'''

roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Michael', 'Everett', 'Lisa', 'Sam', 'Noah']
print(roll[2])
enrolment = len(roll)
roll.append('james')
del roll[2]
roll[4] = 'Mike'
print(roll)

print('')

print('time to make it alphabetical')
del roll[3]
roll[0] = 'Bruce'
print(roll)

del roll[4]
roll[2] = 'Everett'
print(roll)


roll[4] = 'Jessica'
print(roll)

del roll[7]
roll[3] = 'James'
print(roll)

del roll[5]
roll[5] = 'kayley'
print(roll)

roll.append('Lisa')
print(roll)

roll.append('Mike')
print(roll)

roll.append('Noah')
print(roll)

roll.append('Sam')
print(roll)


print('Succesfully alphabetized')
print('')
print('time to reverse')

roll[0] = 'Sam'
roll[1] = 'Noah'
roll[2] = 'Mike'
roll[3] = 'Lisa'
roll[4] = 'Kayley'
roll[5] = 'Jessica'
roll[6] = 'James'
roll[7] = 'Everett'
roll[8] = 'Emily'
roll[9] = 'Bruce'

print(roll)
print('succesfully reversed')
print('')
print('attempt to print random student')

from random import randint
x = randint(0,9)
print(roll[x])

print('atttempt succesful')
