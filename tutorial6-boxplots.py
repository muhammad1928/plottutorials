import numpy as np
import matplotlib.pyplot as plt

# candle chart? maybe not

# # generating 300 heights with mean of 172 and 8 diviation 
# heights = np.random.normal(172, 8, 300)

# plt.boxplot(heights)
# plt.show()

first = np.linspace(0,10, 25)           # creates a data array which starts with 0, ends with 10 and 23 random numbes in between. total 25 numbers
second = np.linspace(10, 200, 25)       # creates a data array which starts with 10, ends with 200 and 23 random numbes in between. total 25 numbers
third = np.linspace(200,210, 25)        # creates a data array which starts with 200, ends with 210 and 23 random numbes in between. total 25 numbers
fourth = np.linspace(210, 230, 25)      # creates a data array which starts with 210, ends with 230 and 23 random numbes in between. total 25 numbers
# print(first, second, third, fourth)

data = np.concatenate((first, second, third, fourth)) # combines all the data above
# print(data)

plt.boxplot(data) # divides the candel chart to 4 pieces, each peace has 25 data, yellow line is the median
plt.show()