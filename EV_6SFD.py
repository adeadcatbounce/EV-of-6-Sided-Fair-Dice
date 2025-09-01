# import libraries and packages

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# the numbers in a six sided fair dice
dice_numbers = np.arange(1,7)
# sum of all numbers in the dice
sum_dice = np.sum(dice_numbers)
# expected value of a six sided fair dice
expected_value = sum_dice/len(dice_numbers)

# specifying the probability of each number in a six sided fair dice
probability_array = np.full(6, 1/6)

# creating trials for dice rolls between one and a million
trials = [10**x for x in range(0,10)]

# printing output : expected value of six sided fair dice

print()
print(f"The expected value of a six sided fair dice roll is {expected_value} \n")

# creating empty lists append - trial runs and sample mean of EV (of a six sided fair dice)
trial = []
EV_array = []

for trials in trials:
    sample = np.random.choice(np.arange(1, 7), size=trials, p=probability_array)
    output = (f"For a total number of {trials:,} dice rolls, " + f"the expected value is {np.mean(sample)}")
    print(output)

# Appending results to empty list
    trial.append(trials)
    EV_array.append(np.mean(sample))

# Create a dataframe
df = pd.DataFrame({'Column1': trial, 'Column2': EV_array}).rename(columns={'Column1' : 'Trials', 'Column2': 'EV'})
df['Trials'] = df['Trials'].apply(lambda x: f'{x:,}')
print(df)

# Plot results
sns.set_style("darkgrid")
plt.title("Expected Value as A Function of - Number of Rolls of A Six Sided Fair Dice", fontsize=12)
sns.barplot(x='EV', y='Trials', data=df, width=1/3)
plt.ylabel("Number of Rolls, of a Six Side Fair Dice", fontsize=12)
plt.xlabel('Expected Value (EV)', fontsize=12)
plt.xticks(np.arange(0,6.5,0.5))
plt.savefig('Output_Plot1.png', bbox_inches = 'tight', dpi=500)
