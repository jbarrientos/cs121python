import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns 
import random
import numpy as np

fig = plt.figure('Roll the Dice')

frequencies = np.zeros(6) #{1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

x = [1,2,3,4,5,6]

#
# This portion of code was taken from the program ran in the 
def update(frame_number, rolls, faces, frequencies):
    """Configures bar plot contents for each animation frame."""
    # roll die and update frequencies
    for i in range(rolls):
        frequencies[random.randrange(1, 7) - 1] += 1 

    # reconfigure plot for updated die frequencies
    plt.cla()  # clear old contents contents of current Figure
    axes = sns.barplot(
        x=faces, 
        y=frequencies, 
        palette='bright', 
        alpha=.7
        )  # new bars
    axes.set_title(f'Die Frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel='Die Value', ylabel='Frequency')  
    axes.set_ylim(top=max(frequencies) * 1.10)  # scale y-axis by 10%

    # display frequency & percentage above each patch (bar)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0  
        text_y = bar.get_height() 
        text = f'{frequency:,}\n{frequency / sum(frequencies):.1%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')
    

num = int(input('How many times to roll the dice?'))
num_dices = int(input('How many dices to roll?'))
    
sns.set_style('whitegrid')  # white backround with gray grid lines
values = list(range(1, 7))  # die faces for display on x-axis
#frequencies = [0] * 6  # six-element list of die frequencies
#print(frequencies)

# configure and start animation that calls function update
die_animation = animation.FuncAnimation(
    fig, update, repeat=False, frames=num - 1, interval=33,
    fargs=(num_dices, values, frequencies))

plt.show()  # display window