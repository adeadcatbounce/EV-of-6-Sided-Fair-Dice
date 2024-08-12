"""
binomial distribution
this code writes a function
to take in inputs for numbers of exact heads needed, in n number of trials
and computes the probability of obtaining those heads in n trials
it assumes the coin to be a fair coin
"""

# import libraries and packages

import numpy as np
from scipy.special import comb

probability_heads = 1/2
probability_tails = 1/2

def binomial(n, heads):
    cases = comb(n, heads)
    probability = cases * (probability_heads**heads) * (probability_tails**(n-heads))
    final_probability = np.round(probability*100, 1)
    return final_probability

# Using the function to estimate the probability of obtaining exactly 7 heads in 10 trials
result = binomial(10, 7)

# printing output : expected value
print()
print(f"The probability of getting a head and tail for a fair coin is {probability_heads} and {probability_heads} \n")
output = (f"The probability of obtaining exactly 7 heads in 10 trials is {result} %")
print(output)
