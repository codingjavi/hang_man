#WAY FASTER TO FIND A NUMBER
def binary_search(array, target, low = None, high = None):
    if low == None:
        low = 0
    if high == None:
        #-1 because we are tyring to find the indices instead of how many numbers
        high = len(array) - 1

    # if target not in this list, hm
    if high < low:
        return -1
    # "//" divides and rounds the number (how many times can 2 go into 7 = 6)
    #mid_point = 5
    mid_point = (low + high) // 2

    #if the target is in the mid_point 
    if array[mid_point] == target:
        return mid_point
    
    #elif keep running it the function BUT the upper half is gone
    #checks target is below(or less than) mid_point
    elif int(target) < array[mid_point]:
        return binary_search(array, target, low, mid_point - 1)
    
    #keep running the function BUT the lower half is gone
    else:
        return binary_search(array, target, mid_point + 1, high)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = input("Choose a number between 1-10 ")
print("You're number was found in the number " + str(binary_search(l, int(target)))+ " position")


