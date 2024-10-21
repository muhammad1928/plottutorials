import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# 3d scatterplot
# telling that it is a 3d plot/projection
ax = plt.axes(projection ="3d")

x = np.random.random(100)   # generating 100 random numbers
y = np.random.random(100)   # generating 100 random numbers
z = np.random.random(100)   # generating 100 random numbers

ax.set_xlabel("x label")    # setting label for x axes
ax.set_ylabel("y label")    # setting label for y axes
ax.set_zlabel("z label")    # setting label for z axes

ax.scatter(x,y,z)           # generating a 3d scatter plot
ax.set_title("3d plot")     # title of plot
plt.show()
