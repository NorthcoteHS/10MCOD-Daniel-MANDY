'''
prog:       beating dice @CSRoll
name:       Daniel Mandy   
date:       2018-04-24
desc:       multiplys bet by three when u lose, receive double bid when u win
'''



#starting variables
coins = int(input('enter an amount of coins you would like to start with: '))
startingbid = int(input('enter a bid you would like to start with: '))

counter = 0
bid = 0
bid = int(bid)
counter = int(counter)
bid = startingbid
highscore = 0
highscore = int(highscore)

#if you have still have money.
while coins > 0:
    
    from random import randint
    roll = randint(0, 48)
    
    #a way to keep track of your money and total rolls
    print(coins)
    if coins > highscore:
        highscore = coins
    
    counter = (counter + 1)
    
    #removes your bid from you balance, if you win you will get it back X2
    coins = (coins - bid)
    
    if roll == 1 or roll == 3 or roll == 5 or roll == 7 or roll == 9 or roll == 11 or roll == 13 or roll == 15 or roll == 17 or roll == 19 or roll == 21 or roll == 23 or roll == 25 or roll == 27 or roll == 29 or roll == 31 or roll == 33 or roll == 35 or roll == 37 or roll == 39 or roll == 41 or roll == 43 or roll == 45 or roll == 47:
        
        #gives you your coins
        coins = coins + bid*2
        
        #reverts your bid back to your starting bid
        bid = startingbid
        
    else: 
        bid = bid*3

        
print(str(counter) + ' rolls')
print('highest coins was ' + str(highscore))
        
    
        
