import numpy as np
import matplotlib.pyplot as plt


# creating 1000 data with mean of 20  and diviation of 1.5
ages = np.random.normal(20,1.5, 1000)
print(ages)

# creating a histogram plot
# bins=20 =  how many columns to show in this case 20
# bins=[ages.min(), 18, 21, ages.max()]  you can also specify the bins urself
# set cumulative to True to get an icreasing graph

plt.hist(ages, bins=[ages.min(), 18, 21, ages.max()], cumulative=True)
plt.show()