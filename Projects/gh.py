import random

user_input = input("Pick an option, rock, paper or scissors): ")
can_input = ["rock", "paper", "scissors"]
computer_input = random.choice(can_input)
print("You chose", user_input, "and computer chose", computer_input)

if user_input == computer_input:
    print("Both players selected", user_input, ". It's a tie.")
elif user_input == "rock":
    if computer_input == "scissors":
        print("Rock smashes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user_input == "paper":
    if computer_input == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user_input == "scissors":
    if computer_input == "paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock smashes scissors. You lose.")