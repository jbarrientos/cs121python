# -*- coding: utf-8 -*-
"""
Date: Thu Feb 23 17:57:56 2023
Instructor: Kaleab Gorfu
Student: Jorge Barrientos
CS 121: Python for DS and ML
"""
from statistics import mean       

print('+-------------------------------------------------------------+')
print('| Program to calculate numbers with Python built in functions | ') 
print('+-------------------------------------------------------------+')

numbers = int(input('How many numbers do you want to calculate? (type 0 to exit) '))

numsList = []
numsRow = ''
runningTotal = 0

for i in range(numbers):
    strNum = ''
    cont = True
    num = 0
    while cont:        
        strNum = input('Please enter the number '+str(i+1) + ': ')
        num = float(strNum)        
        if num == 0:
            print('Please type a number different from zero.')
            continue
        else:
            #
            cont = False
            numsList.append(num)
            #
            if i == numbers - 1:
                numsRow += str(num)
            else:
                numsRow += str(num) + ','
        
        
            
if len(numsList) > 0:  
    print('-------------------------------------------')   
    print('Display each number in a row (Horizontally)')   
    print('-------------------------------------------')   
    print(numsRow)
    print('--------------------------------------------------')   
    print('Display each number in a row by itself(Vertically)')   
    print('--------------------------------------------------')   
    for num in numsList:
        print(num)

    print('-------------------------------')
    print('RUNNING TOTAL: ' + str(sum(numsList)))
    print('MIN NUMBER: ' + str(min(numsList)))
    print('MAX NUMBER: ' + str(max(numsList)))
    print('AVERAGE: ' + str(mean(numsList)))
    print('-------------------------------')
    

   
    

