'''
Prog:   Music scales CAT3.py
Name:   Daniel Mandy  
Date:   6/6/2018
Desc:   shows the user the notes in a particular scale
'''
C = 1
Db = 2
D = 3
Eb = 4
E = 5
F = 6
Gb = 7
G = 8
Ab = 9
A = 10
Bb = 11
B = 12

C = int(C)
Db = int(Db)
D = int(D)
Eb = int(Eb)
E = int(E)
F = int(F)
Gb = int(Gb)
G = int(G)
Ab = int(Ab)
A = int(A)
Bb = int(Bb)
B = int(B)


scaletype = input('Please enter a type of scale(major): ')
key = input('Please enter the starting note(use flats only No sharps eg Db or Bb): ')




if key == 'C':
    key = 1
    
if key == 'Db':
    key = 2
    
if key == 'D':
    key = 3
    
if key == 'Eb':
    key = 4
    
if key == 'E':
    key = 5
    
if key == 'F':
    key = 6
    
if key == 'Gb':
    key = 7
    
if key == 'G':
    key = 8
    
if key == 'Ab':
    key = 9
    
if key == 'A':
    key = 10
    
if key == 'Bb':
    key = 11
    
if key == 'B':
    key = 12
    
if scaletype == major:
    note1 = key
    note2 = key+2
    note3 = key+4
    note4 = key+5
    note5 = key+7
    note6 = key+9
    note7 = key+11
    note8 = key

if note1 == 1:
    note1 = 'C'
    
if note1 == 2:
    note1 = 'Db'
    
if note1 == 3:
    note1 = 'D'
    
if note1 == 4:
    note1 = 'Eb'
    
if note1 == 5:
    note1 = 'E'
    
if note1 == 6:
    note1 = 'F'
    
if note1 == 7:
    note1 = 'Gb'
    
if note1 == 8:
    note1 = 'G'
    
if note1 == 9:
    note1 = 'Ab'
    
if note1 == 10:
    note1 = 'A'
    
if note1 == 11:
    note1 = 'Bb'
    
if note1 == 12:
    note1 = 'B'
    
if note1 == 13:
    note1 = 'D'
   






























