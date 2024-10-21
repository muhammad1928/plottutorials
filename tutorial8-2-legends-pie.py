import numpy as np
import matplotlib.pyplot as plt



# creating data for 3 dataset
votes = [10, 2, 5, 17, 22, 10, 11]
people= ['A', 'B', 'C', 'D', 'E', 'F', 'G']

plt.pie(votes, labels=None)
plt.legend(people, loc="upper right")
# showing the graphs
plt.show()



