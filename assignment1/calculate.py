# -*- coding: utf-8 -*-
"""
Date: Thu Feb 23 17:57:56 2023
Instructor: Kaleab Gorfu
Student: Jorge Barrientos
Changes:
    03/11/2023: Include central tendency functions: calcMean, calcMedian and calcMode
CS 121: Python for DS and ML
"""
# Functions
def calcTotal(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calcMin(numbers):
    minNumber = 0
    
    if len(numbers) > 0:
        minNumber = numbers[0]
        
    for num in numbers:
        if num < minNumber:
            minNumber = num
    return minNumber

def calcMax(numbers):
    maxNumber = 0
    
    if len(numbers) > 0:
        maxNumber = numbers[0]
        
    for num in numbers:
        if num > maxNumber:
            maxNumber = num
            
    return maxNumber

def calcAvg(numbers):
    return calcTotal(numbers) / len(numbers)

def calcMean(numbers):
    return calcTotal(numbers) / len(numbers)

def calcMedian(numbers):
    sortedList = numbers
    sortedList.sort()
    numbersLength = len(sortedList)
    if numbersLength % 2 == 0:          
        startIdx = int(numbersLength / 2) - 1
        endIdx = int((numbersLength / 2))              
        #print('startIdx',startIdx)
        #print('endIdx',endIdx)
        #print(sortedList)
        medianVal = calcTotal([sortedList[startIdx],sortedList[endIdx]]) / 2.0
    else:
        midIndex = len(sortedList) // 2
        medianVal = sortedList[midIndex]        
        
    return medianVal

def calcMode(numbers):
    modeDict = {}
    for num in numbers:
        strNum = str(num)
        if strNum in modeDict:
            modeDict[strNum] += 1
        else:
            modeDict[strNum] = 1
            
    #print('mode', modeDict.values())
    #print(modeDict)
    modeVal = 0.0
    modeKey = ''
    
    for key in modeDict:
        print(key)
        if(modeDict[key] > modeVal):
            modeVal = modeDict[key]
            modeKey = key
            
            
    return modeKey
    

print('+--------------------------------------------------------+')
print('| Program to calculate numbers using self made functions | ') 
print('+--------------------------------------------------------+')
        
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
    print('RUNNING TOTAL: ' + str(calcTotal(numsList)))
    print('MIN NUMBER: ' + str(calcMin(numsList)))
    print('MAX NUMBER: ' + str(calcMax(numsList)))
    print('AVERAGE: ' + str(calcAvg(numsList)))
    print('MEAN: ' + str(calcMean(numsList)))
    print('MEDIAN: ' + str(calcMedian(numsList)))
    print('MODE: ' + str(calcMode(numsList)))
    print('-------------------------------')
    
    

   
    

