import random

def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(["N", "S", "E", "W"])
        if step == "N":
            y = y + 1
        elif step == "S":
            y = y - 1
        elif step == "E":
            x = x +1
        else:
            x = x -1
    return (x,y)
    
i = input("How much would you like to walk? ")
walk = random_walk(int(i))
print (walk),
print (abs(walk[0]) + abs(walk[1]))

    