import numpy as np
import matplotlib.pyplot as plt


# tutorial 3 Bar plots
# categorical data
x = ["C++", "C#", "Python", "Java", "Go"]
y = [20, 50, 140, 7, 56]


# align="edge" (this makes the pointer start at the starting corner of bar)
# edgecolo="green" (border color)
# lw=6 (border width 6)
plt.bar(x, y, color="red", align="edge", width=0.6, edgecolor="green", lw=6)
plt.show()