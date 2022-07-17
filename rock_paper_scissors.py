import random
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]
while True:
    user_pick = input("Choose Rock/Paper/Scissors or Q to quit ").lower()
    if user_pick == "q":
        break
    if user_pick not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked ", computer_pick)

    if user_pick == "rock" and computer_pick == "scissors":
        print ("you won")
        user_wins+=1
        continue

    elif user_pick == "paper" and computer_pick == "rock":
        print ("you won")
        user_wins+=1
        continue

    elif user_pick == "scissors" and computer_pick == "paper":
        print ("you won")
        user_wins+=1
        continue

    else: 
        print("you lose")
        computer_wins+=1

print("You won " + str(user_wins))
print("The computer won "+ str(computer_wins))

