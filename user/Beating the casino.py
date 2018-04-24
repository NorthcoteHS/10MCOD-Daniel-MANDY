'''
Prog:      Beating the casino
Name:      Daniel Mandy
Date:      15/2/2018
desc:      creates a simulation of a certain strategy to beat a roulette table at a casino. also lets you view how you are doing once a certain amount of rolls happen
'''
bidcalc = 0
statscounter = 0
keepgoing = 'yes'
bidtracker = 0
wintracker = 0
losstracker = 0

#starting values of money and bid
money = int(input('Enter an amount of tokens you would like to start with: '))
bid = int(input('Enter a starting bid amount: '))

#makes all these variables intergers
bidcalc = int(bidcalc)
bidtracker = int(bidtracker)
statscounter = int(statscounter)
wintracker = int(wintracker)
losstracker = int(losstracker)

while money > 0:

    #deducts the current bid from money
    #money = (money - bid)

    while keepgoing == 'yes':
    
    #essentially rolls the wheel
        from random import randint
        x = randint(0, 18)
        
        money = (money - bid)

        #if you win you get double the money you met, eg bet 1 dollar, win back 2.
        if x == 1 or x == 3 or x == 5 or x == 7 or x == 9 or x == 11 or x == 13 or x == 15 or x == 17: 
            money = money + bid*2
            bid = bid/2**bidcalc
            bidcalc = 0
            #print(money)
        
            bidtracker = bidtracker + 1
            statscounter = statscounter + 1
            wintracker = wintracker + 1
            
            if statscounter > 199:
                print('your money is' + str(money))
                print('you have made ' + str(bidtracker) + ' bids')
                print('you have won ' + str(wintracker) + ' rolls')
                print('you have lost ' + str(losstracker) + ' rolls')
            
                keepgoing = input('do you want to continue playing:(yes/no) ')
                if keepgoing == 'no':
                    print('Thank you for playing')
                elif keepgoing == 'yes':
                    print('good luck')
                else:
                    keepgoing = input('do you want to continue playing:(yes/no) ')    
                    statscounter = statscounter - 200

        #if you lose makes your bid double the size    
        else:
            bid = bid*2
            bidcalc = bidcalc + 1
            
        
            bidtracker = bidtracker + 1
            statscounter = statscounter + 1
            losstracker = losstracker + 1
            
            if statscounter > 199:
                print('your money is' + str(money))
                print('you have made ' + str(bidtracker) + ' bids')
                print('you have won ' + str(wintracker) + ' rolls')
                print('you have lost ' + str(losstracker) + ' rolls')
            
                keepgoing = input('do you want to continue playing:(yes/no) ')
                if keepgoing == 'no':
                    print('Thank you for playing')
                elif keepgoing == 'yes':
                    print('good luck')
                else:
                    keepgoing = input('do you want to continue playing:(yes/no) ')
                    statscounter = statscounter - 200
            
print('game over!')        
