import random

top_of_range  = input("Type a number ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than 0 next time")
        quit()
else:
    print("Please type a number greater than 0 next time")
    quit()

random_number = random.randint(0, top_of_range)
 
while True:
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)

    else:
        print("Please type a number next time")
        continue

    if guess == random_number:
        print ("you got it")
        break
    else:
        print ("you're wrong")




       
