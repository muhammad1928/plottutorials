import numpy as np
import matplotlib.pyplot as plt


# tutorial 1 
# big data
X_data = np.random.random(1250) * 100 # generating random data
Y_data = np.random.random(1250) * 100 # generating random data

# creating a scatterplot (bunch of dots on the graph) 
# c="color" / c = "#431234"
# markers ="*" (not dots but stars)
# s = 15 (size of the  markers)
# alpha ="0.3" makes it darker or lighter color if the data overlapse
plt1 = plt.scatter(X_data, Y_data, c="blue", marker="*", s=150, alpha=0.3 )

# small data
X_data = np.random.random(50) * 100 # generating random data
Y_data = np.random.random(50) * 100 # generating random data
plt1 = plt.scatter(X_data, Y_data, c="blue", marker="*", s=150)
plt.show()


# generating 1000 ages with a mean of 20, and 1.5 deviation (sapma)
ages = np.random.normal(20, 1.5, 1000)
print(round(ages,1))
