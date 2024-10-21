## CAUTION!!! this code will run til its finished
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

# we are going to flip a coin (50/50)
heads_tails = [0, 0, 0]
for _ in range(1000):
    heads_tails[random.randint(0,2)] +=1 # if random number is 0, heads increase, if 1 tails increase.

    # creating a bar plot, with head and tail labels, passing heads_tails value. coloring the bars using a list
    plt.bar(["heads", "tails", "others"], heads_tails, color=["red", "blue", "green"])
    plt.pause(0.0001) # puase 1ms  (animate)
plt.show