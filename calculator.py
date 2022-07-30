def addition():
    first_num = float(input("Enter a whole number to add "))
    ans = 0
    second_num = float(input("Enter a second whole number to calculate "))
    ans = first_num + second_num
    return ans

def subtraction():
    first_num = float(input("Enter a whole number to subtract "))
    ans = 0
    second_num = float(input("Enter a second whole number to calculate "))
    ans = first_num - second_num
    return ans

def multiplication():
    first_num = float(input("Enter a whole number to multiply "))
    ans = 0
    second_num = float(input("Enter a second whole number to calculate "))
    ans = first_num * second_num
    return ans

def division():
    first_num = float(input("Enter a number to divide "))
    ans = 0
    second_num = float(input("Enter a second whole number to calculate "))
    ans = first_num / second_num
    return ans

print("Hello welcome to my calculator!")
print("pick a for addition")
print("pick s for subtraction")
print("pick m for multiplication")
print("pick d for division")
print("pick q to quit")
choice = input("")

if choice == "a":
    print("Ans = " + str(addition()))

elif choice == "s":
    print("Ans = " + str(subtraction()))

elif choice == "m":
    print("Ans = " + str(multiplication()))

elif choice == "d":
    print("Ans = " + str(division()))

elif choice == "q":
    quit

else:
    print ("Sorry invalid integer")
    quit




