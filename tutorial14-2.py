import numpy as np
import matplotlib.pyplot as plt
import random

# Initialize counts for each side of a six-sided die
dice_counts = [0, 0, 0, 0, 0, 0]

# Set up the bar chart
plt.figure()
bars = plt.bar(["1", "2", "3", "4", "5", "6"], dice_counts, color=["orange", "yellow", "green", "blue", "purple", "red"])
plt.ylim(0, 200)  # Set y-axis limit to better visualize changes

# Roll the die 1000 times
for _ in range(1000):
    roll = random.randint(1, 6)
    dice_counts[roll - 1] += 1

    # Update bar heights
    for i, bar in enumerate(bars):
        bar.set_height(dice_counts[i])

    plt.pause(0.001)  # Pause to animate

plt.show()
