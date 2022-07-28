from mpl_toolkits import mplot3d #making a 3d graph
import numpy as np #used for the arrays of 0s
import matplotlib.pyplot as plt #still using to make graph
import random #for random.choice

fig = plt.figure() #makes the graph
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')

def randomwalk(n):
    x = np.zeros(n) #makes arrays to store information later
    y = np.zeros(n)
    z = np.zeros(n)

    for i in range(1, n): #starts at 1 bc we start at (0,0)
        step = random.choice(["N", "S", "E", "W", "I", "O"])
        if step == "E":
            x[i] = x[i - 1] + 1 #using brakets to do something with the arrays(like x[1] would go the first value of the array)
            y[i] = y[i - 1] #replaces the arrays of zeros with values
            z[i] = z[i - 1] #z[i-1] because we are copiying the previus value
        elif step == "W":
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
            z[i] = z[i - 1]
        elif step == "N":
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
            z[i] = z[i - 1]
        elif step == "S":
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
            z[i] = z[i - 1]
        elif step == "I":
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
            z[i] = z[i - 1]
        elif step == "O":
            x[i] = x[i - 1]
            y[i] = y[i - 1]
            z[i] = z[i - 1] - 1

    return (x,y,z)

x_data, y_data, z_data = randomwalk(100) #the function creates 2 outputs and we're saving these out puts here

print (x_data) #They're just arrays with values instea of 0s
print (y_data)
print (z_data)

#plotting
ax.plot3D(x_data, y_data, z_data, "green")
ax.set_title('3D Random Walk')
plt.show()