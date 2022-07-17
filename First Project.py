print ("Welcome to my computer game")

play = input("Do you want to play my game ")

if play.lower() != "yes":
    quit()

print ("Okay lets play")
score = 0
question = input("Who was the first President? ")
if question == "George Washington":
    print ("Corrent")
    score=+ 1
else:
    print("Incorrect")

question = input("What does CPU stand for? ")
if question == "central processing unit":
    print ("Correct")
    score= score + 1
else:
    print("Incorrect")

question = input("What does GPU stand for? ")
if question == "graphics processing unit":
    print ("Correct")
    score= score + 1
else:
    print("Incorrect")

question = input("What does RAM stand for? ")
if question == "random access memory":
    print ("Correct")
    score= score + 1
else:
    print("Incorrect")

question = input("What does PSU stand for? ")
if question == "power supply":
    print ("Correct")
    score= score + 1
else:
    print("Incorrect")

print ("You got " + str(score) + " questions correct")
print ("You got " + str((score / 5) * 100) + "%")