'''
Program:      SingleWordPigLatin.py  
Name:         Daniel Mandy
Date:         28/2/2018
desc:         create a program that outputs pig latin from whatever the input is
'''
# x gives something to loop for. x is irrelivant to rest of code, only used in loop
x = 1
while x == 1:
#puts ay at the end of words that start with vowels.
    aa = input('enter a word: ')
    if aa[0] == 'a' or aa[0] == 'e' or aa[0] == 'i' or aa[0] == 'o' or aa[0] == 'u':
        print(aa + 'ay')
    #puts the first letter at the end of the world and adds 'ay'.
    else:
        aa = aa + aa[0]
        firstLetter = (aa[0])
        aa = aa.replace((aa[0]), '')
        aa = aa + firstLetter
        aa = aa + 'ay'
        print(aa)
