import numpy as np
import matplotlib.pyplot as plt


years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

income = [55, 56, 62, 61, 72, 72, 73, 75]

# y axes which will include all the income data from 55 to 75
income_tickets = list(range(50,81,2)) # creating a list from 50 to 81 adding 2 each time.
# print(income_tickets)


plt.plot(years, income)
# title of plot, adding style, size to 30 and font family
plt.title("Income of John (in USD)", fontsize=30, fontname="arial")   
# title of plot, adding style, size to 30 and font family          
plt.xlabel("Year")                                                              # x label 
plt.ylabel("Yearly income in USD")                                              # y label
# the function will loop tru income_tickets list and add $ sight before all the data and k usd after
plt.yticks(income_tickets, [f"${x}k USD" for x in income_tickets])              # y label points
plt.show()