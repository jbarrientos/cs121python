# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:33:22 2023

@author: jbarr
"""
import random



cont = True
randomNumber = random.randint(1, 10)

while cont:
    playerNumber = int(input('Guess Any Number 1 To 10. To Exit type 0: '))
    
    if playerNumber == 0:
        print('Bye, thanks for playing!')
        cont = False
    elif playerNumber > 10 or playerNumber < 0:
        print('Please type a valid Number 1 To 10 or 0 to Exit.')
    else:        
        #
        if randomNumber == playerNumber:
            print('You win! :o)')
        elif randomNumber > playerNumber:
            print('Too low')
        elif randomNumber < playerNumber:
            print('Too high')
            
            
    