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

plt.tight_layout() # this will make the plot to not overlaps eachother


# to export we call plt.savefig
# this will save the file to the same folder as this python file
# dpi 300 will increase the resolution
# transparent = True deletes the background color, it is false by default
# bbox_inches cuts away the paddings
# pad_inches adds padding
plt.savefig("img/tutorial12-export-plots", dpi=600, transparent=False, bbox_inches="tight", pad_inches=0.2) 
