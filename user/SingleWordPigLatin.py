'''
Program:      SingleWordPigLatin.py  
Name:         Daniel Mandy
Date:         28/2/2018
desc:         create a program that outputs pig latin from whatever the input is(single word form with unlimited constananst at the start)
'''
# x gives something to loop for. x is irrelivant to rest of code, only used in loop

#puts ay at the end of words that start with vowels.
bb = 'yes'
aa = input('Enter a word: ')
while bb == 'yes':


        if aa[0] == 'a' or aa[0] == 'e' or aa[0] == 'i' or aa[0] == 'o' or aa[0] == 'u':
            print(aa + 'ay')
            bb = 'no'
            cc = input('do you want to enter another word?(yes/no) ')
            if cc == 'yes':
                aa = input('Enter another word: ')
                bb = 'yes'
            if cc == 'no':
                print('Thanks for you time!')
            else:
                print('type properly plz!')

            #puts the first letter at the end of the world and adds 'ay'.
        else:
            aa = aa + aa[0]
            firstLetter = (aa[0])
            aa = aa.replace((aa[0]), '')
            aa = aa + firstLetter


