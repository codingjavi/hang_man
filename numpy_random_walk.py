import numpy as np
import matplotlib.pyplot as plt
import random

def randomwalk(n):
    x = np.zeros(n) #makes arrays to store information later
    y = np.zeros(n) 

    for i in range(1, n): #starts at 1 bc we start at (0,0)
        step = random.choice(["N", "S", "E", "W"])
        if step == "E":
            x[i] = x[i - 1] + 1 #using brakets to do something with the arrays(like x[1] would go the first value of the array)
            y[i] = y[i - 1] #replaces the arrays of zeros with values
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

x_data, y_data = randomwalk(10) #the function creates 2 outputs and we're saving these out puts here
print (x_data) #They're just arrays with values instea of 0s
print (y_data)

plt.title("2D Random Walk in Python") #use matplot lib to create a graph of the walk
plt.plot(x_data, y_data) #plug in the 2 out puts(arrays) we got from the function(plugging in the arrays we got)
plt.show()






