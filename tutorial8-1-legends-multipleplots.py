import numpy as np
import matplotlib.pyplot as plt



# creating data for 3 dataset
stock_a = [100, 102, 99, 101, 101, 100 ,102]
stock_b = [90, 95, 102, 104, 105, 103, 109]
stock_c = [110, 115, 100, 105, 100, 98, 95]


# creating 3 different graphs
# label is giving the graphs a name
plt.plot(stock_a, label="stock a")
plt.plot(stock_b, label="stock b")
plt.plot(stock_c, label="stock c")

# this will activate the labels
# loc = give the position of the labels
plt.legend(loc="lower right")

# showing the graphs
plt.show()



