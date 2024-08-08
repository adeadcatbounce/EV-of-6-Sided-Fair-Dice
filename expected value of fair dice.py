"""
this code shows
that with increasing number of trials from 1 to a billion
the expected value of rolls from a six sided fair dice
gets closer and closer to the theoretical value of ~ 3.5
"""

# import libraries and packages

import numpy as np

# the numbers in a six sided fair dice
dice_numbers = np.arange(1,7)
# sum of all numbers in the dice
sum_dice = np.sum(dice_numbers)
# expected value of a six sided fair dice
expected_value = sum_dice/len(dice_numbers)

# specifying the probability of each number in a six sided fair dice
probability_array = np.full(6, 1/6)

# creating trials for dice rolls between one and a billion
trials = [10**x for x in range(0,6)]

# printing output : expected value

print()
print(f"The expected value of a six sided fair dice roll is {expected_value} \n")

for trials in trials:
    sample = np.random.choice(np.arange(1, 7), size=trials, p=probability_array)
    output = (f"For a total number of {trials:,} dice rolls, " + f"the expected value is {np.mean(sample)}")
    print(output)