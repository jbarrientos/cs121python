# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:33:22 2023

@author: jbarr
"""
import random



cont = True

while cont:
    guess = int(input('Guess Heads(1) Or Tails(2). To Exit type 0: '))
    
    if guess == 0:
        print('Bye, thanks for playing!')
        cont = False
    elif guess > 2:
        print('Please type a valid option: Heads(1), Tails(2) or 0 to Exit.')
    else:
        randomFlip = random.randint(1, 2)
        #print(randomFlip, guess)
        #
        if randomFlip == guess:
            print('You win! :o)')
        else:
            print('Sorry, you loose :o(')
            
            
    