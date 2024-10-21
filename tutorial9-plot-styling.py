import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("dark_background") # change background
# for more styles visit
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
# for custom styles visit
# https://matplotlib.org/stable/users/explain/customizing.html#customizing

# creating data for 3 dataset
votes = [10, 2, 5, 17, 22, 10, 11]
people= ['A', 'B', 'C', 'D', 'E', 'F', 'G']

plt.pie(votes, labels=None)
plt.legend(people, loc="upper right")
# showing the graphs
plt.show()



