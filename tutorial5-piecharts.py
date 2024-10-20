import numpy as np
import matplotlib.pyplot as plt
import random




# we ask what programming language u use and what programming language is ur favourite, you can only choose 1 fav 
langs = ["Python", "C++", "Java", "C#", "Gp" ]
votes = []

explodes = [0, 0, 0.2, 0.5, 0] # distance to the pie center

# generating random numbers
for x in range (5):
    y = round(random.random() * 100)
    votes.append(y)
    x += 1


# creating a pie plot
# explode makes the plot separate
# autopct show the procent of the votes
# pctdistance is the distance of procentage from pie center
# startangle = chooses where the plot starts. this starts at 90 degree, counter clockwise
plt.pie(votes, labels=langs, explode=explodes, autopct="%.2f%%", pctdistance=1.3, startangle=90)
plt.show()