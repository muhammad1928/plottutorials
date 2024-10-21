import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# 3d scatterplot
# telling that it is a 3d plot/projection
ax = plt.axes(projection ="3d")

x = np.arange(0, 50 ,0.1)       # generating numbers from 0 to 50, stepsize 0.1 (0.0, 0.1, 0.2 ...)
y = np.sin(x)                   # sinus of x
z = np.cos(x)                   # Cosinus of x

# ax.set_xlabel("x label")    # setting label for x axes
# ax.set_ylabel("y label")    # setting label for y axes
# ax.set_zlabel("z label")    # setting label for z axes

ax.plot(x,y,z)           # generating a 3d scatter plot
# ax.set_title("3d plot")     # title of plot
plt.show()
