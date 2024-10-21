import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# 3d scatterplot
# telling that it is a 3d plot/projection
ax = plt.axes(projection ="3d")

x = np.arange(-5, 5 ,0.1)
y = np.arange(-5, 5 ,0.1)

X, Y = np.meshgrid(x,y)
# [[-5, -4.9, - 4.8, ..., 4.8, 4.9]..(3 more times)..[-5, -4.9, - 4.8, ..., 4.8, 4.9]] ..(3 more times) .. [[-5, -4.9, - 4.8, ..., 4.8, 4.9]..(5 times total)..[-5, -4.9, - 4.8, ..., 4.8, 4.9]]
# print(X, Y)

Z = np.sin(X) * np.cos(Y)

# to plot the surface
ax.plot_surface(X,Y,Z, cmap="Spectral")
ax.set_title("3D surface plot")
ax.set_xlabel("x label")
ax.set_ylabel("y label")    
ax.set_zlabel("z label")
# we can set the starting view point by
# azimuth 15 degree , elevation is 45 degree
ax.view_init(azim=15, elev=45)
plt.show()