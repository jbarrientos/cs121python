# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:10:19 2023

@author: jbarr
"""
import matplotlib.pyplot as plt
import seaborn as sns
import random

results = [0,0,0,0,0,0] #{1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

x = [1,2,3,4,5,6]


#print(results)

def showChart():
    # Set Style
    sns.set_style('darkgrid')
    # Barplot
    barChart = sns.barplot(
        x=x, 
        y=results,         
        errorbar="sd", 
        alpha=.7,
        label='Die face'
        )
    plt.title('Roll die results')
    plt.show()


def rollThedice(times):
    
    for roll in range(times):
        face = random.randrange(1, 7)
        results[face-1] = results[face-1] + 1


num = int(input('How many times to roll the dice?'))
rollThedice(num)
showChart()

