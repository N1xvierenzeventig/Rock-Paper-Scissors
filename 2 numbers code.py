import random

options = ["Rock", "Scissors", "Paper"]

def play():
    while True:
        computer_choice = random.choice(options)
        your_choice = input("What do you pick: Rock, Paper or Scissors? ")
        if your_choice not in options:
            print("Please play by rules and choose a real option.")
        elif your_choice == computer_choice:
            print(f"That's a draw. Your opponent's pick was {computer_choice}.")
        elif (your_choice == "Scissors" and computer_choice == "Paper" ) or (your_choice == "Paper" and computer_choice == "Rock") or (your_choice == "Rock" and computer_choice == "Scissors"):
            print(f"You've won the game, your opponent's pick was {computer_choice}.")
        else:
            print(f"You've lost the game, your opponent's pick was {computer_choice}.")
        a = input("Do you want to continue playing the game? (Yes/No) : ")
        if a.upper() == "NO":
            break




play()


