# -*- coding: utf-8 -*-
"""
Date: Thu Feb 23 17:57:56 2023
Instructor: Kaleab Gorfu
Student: Jorge Barrientos
CS 121: Python for DS and ML
Changes:
    03/11/2023: Include builin central tendency functions: mean, median and mode
"""
from statistics import mean, mode, median       

print('+-------------------------------------------------------+')
print('| Program to calculate numbers using builtin functions | ') 
print('+------------------------------------------------------+')
        
# Ask the user how many numbers wants to process
numbers = int(input('How many numbers do you want to calculate? (type 0 to exit) '))

# Variable to store the list of numbers that the user will enter.
numsList = []
numsRow = ''

# Loop to ask the users the numbers to be processed, 
# according to the quantity of numbers entered by the user 
for i in range(numbers):
    strNum = ''
    cont = True
    num = 0
    # While loop in cases where the user enter a zero value, 
    # the program will ask for a different number.
    while cont:        
        # Ask the number n
        strNum = input('Please enter the number '+str(i+1) + ': ')
        num = float(strNum)        
        if num == 0:
            print('Please type a number different from zero.')
            continue
        else:
            #
            cont = False
		# Append the entered number to the numbers list.
            numsList.append(num)
            # Code to build the string that will have all the entered numbers in one line.
            if i == numbers - 1:
                numsRow += str(num)
            else:
                numsRow += str(num) + ','
        
        
# Evaluate if the list of numbers has at least one number.
if len(numsList) > 0:  
    # This code will be executed only if the listof number has at leat one element.
    print('-------------------------------------------')   
    print('Display each number in a row (Horizontally)')   
    print('-------------------------------------------')   
    print(numsRow)
    print('--------------------------------------------------')   
    print('Display each number in a row by itself(Vertically)')   
    print('--------------------------------------------------')   
    for num in numsList:
        print(num)
    # Display values returned by the functions created above.

    print('-------------------------------')
    print('RUNNING TOTAL: ' + str(sum(numsList)))
    print('MIN NUMBER: ' + str(min(numsList)))
    print('MAX NUMBER: ' + str(max(numsList)))
    print('AVERAGE: ' + str(mean(numsList)))
    print('MEAN: ' + str(mean(numsList)))
    print('MEDIAN: ' + str(median(numsList)))
    print('MODE: ' + str(mode(numsList)))
    print('-------------------------------')
    

   
    

