import random
while True:
    # The following code lines creates the computers choice

    computer_choices = ["rock", "paper", "scissors"]
    computer = random.choice(computer_choices)

    # The following code lines invites the player to choose their hand. The while loop is
    # there so that the player can't choose alternatives outside of rock, paper or scissors

    user = None
    while user not in computer_choices:
        user = input("What's your choice?: ").lower() # so it doesn't matter if the player writes in lower-case, upper-case or a combination

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
            
    # The following code lines lets the program ask the player if they want to play again
    try_again = input("Want to play again?: ").lower()
    if try_again != "yes":
        break

print("Then see you later!")