import random

computer_choices = ["rock", "paper", "scissors"]
computer = random.choice(computer_choices)
user = input("What's your choice?:")

if computer == user:
    print("Computer: ", computer)
    print("You: ", user)
    print("It's a draw :|")
elif computer == "rock":
    if user == "paper":
        print("Computer: ", computer)
        print("You: ", user)        
        print("You won :)")
    elif user == "scissors":
        print("Computer: ", computer)
        print("You: ", user)        
        print("You lose :(")
elif computer == "paper":
    if user == "rock":
        print("Computer: ", computer)
        print("You lose :(")
    elif user == "scissors":
        print("Computer: ", computer)
        print("You: ", user)        
        print("You win :)")
elif computer == "scissors":
    if user == "paper":
        print("Computer: ", computer)
        print("You: ", user)        
        print("You lose :(")
    elif user == "rock":
        print("Computer: ", computer)
        print("You: ", user)        
        print("You win :)")