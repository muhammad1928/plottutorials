import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# array from 0 to 99
x = np.arange(100)

# 2x2 subplots, total 4 grid plots
fig, axs = plt.subplots(2, 2)

# first subplot
axs[0, 0].plot(x,np.sin(x)) # sinus of x
axs[0, 0].set_title("Sinus of x") # title for subplot

# second subplot
axs[0, 1].plot(x,np.cos(x)) # sinus of x
axs[0, 1].set_title("Cosinus of x") # title for subplot

# third subplot
axs[1, 0].plot(x,np.tan(x)) # tanjant of x
axs[1, 0].set_title("Tanjant of x") # title for subplot

# fourth subplot
axs[1, 1].plot(x,np.log(x)) # sinus of x
axs[1, 1].set_title("Logarithm of x") # title for subplot
axs[1, 1].set_xlabel("TEST") # setting fourth plot x label to TEST


fig.suptitle("Four plots") # title for all 
plt.show()

