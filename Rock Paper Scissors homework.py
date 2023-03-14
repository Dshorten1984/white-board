import random

actions = ["Rock", "Paper", "Scissors"]

while True:
    computer_action = random.choice(actions)
    player_action = input("Enter a choice (Rock, Paper, Scissors) or 'I quit' to exit: ")
    
    if player_action == "I quit":
        print("Thank you for playing!")
        break
    
    if player_action not in actions:
        print("Invalid choice. Try again.")
        continue
    
    print(f"\nYou chose {player_action}, computer chose {computer_action}.\n")
    
    if player_action == computer_action:
        print(f"Both players selected {player_action}. It's a tie!")
    elif player_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
