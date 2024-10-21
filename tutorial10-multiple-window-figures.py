import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


# plot multiple side by side
# generating 100 random numbers as x1 and y1
x1, y1 = np.random.random(100), np.random.random(100)
# print(x1, y1)
# generate array from 100 data starting from 0
x2, y2, = np.arange(100), np.random.random(100)
# print(x2)

# creating first window
plt.figure(1)
plt.scatter(x1,y1)

# creating second window
plt.figure(2)
plt.plot(x2,y2)

plt.show()