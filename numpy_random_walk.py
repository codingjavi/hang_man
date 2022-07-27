import numpy as np
import matplotlib.pyplot as plt
import random

def randomwalk(n):
    x = np.zeros(n)
    y = np.zeros(n)

    for i in range(1, 2):
        step = random.choice(["N", "S", "E", "W"])
        if step == "E":
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif step == "W":
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif step == "N":
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        elif step == "S":
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
    
    return (x,y)

x_data, y_data = randomwalk(2)

plt.title("2D Random Walk in Python")
plt.plot(x_data, y_data)
plt.show()






