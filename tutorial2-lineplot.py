import numpy as np
import matplotlib.pyplot as plt


# tutorial 2 
# creating years data 2006 + all the years up to +16
years = [2006 + x for x in range(16)]
# print(years) # [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

weight = [80,84, 89,90,91,94,95,91,108,109,106,108,101,98, 99,105]
# print(len(weight)) # 16
# print(len(years)) # 16

# creating a line chart
# color r
# lw = 3 (line thickness)
# linestyle = "--" (line type = '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted')
# 
plt.plot(years, weight, color="r", lw=3, linestyle="--")
plt.show()

