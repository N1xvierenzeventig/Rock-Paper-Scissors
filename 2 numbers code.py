import random

list = ["Rock", "Scissors", "Paper"]


def play():
    global a, b, Want_To_Play
    Want_To_Play = True
    while Want_To_Play == True:
        a = random.randint(0, 2)
        b = input("What do you choose rock, paper or scissors?: ")
        a = list[a]
        l = f"Unfortunately you've lost the game your opponent had a {a}."
        w = f"Congrats you've won the game your opponent had a {a}."
        d = f"It is a draw, both of you had a {a}."
        if b == "Rock" and a == "Rock":
            print(d)
            p = input("Do you want to play a game once more: ")
            if p == "Yes":
                Want_To_Play = True
            elif p == "No":
                Want_To_Play = False
        elif b == "Paper" and a == "Paper":
            print(d)
            p = input("Do you want to play a game once more: ")
            if p == "Yes":
                Want_To_Play = True
            elif p == "No":
                Want_To_Play = False
        elif b == "Scissors" and a == "Scissors":
            print(d)
            p = input("Do you want to play a game once more: ")
            if p == "Yes":
                Want_To_Play = True
            elif p == "No":
                Want_To_Play = False
        elif b == "Rock" and a == "Paper":
            print(l)
            p = input("Do you want to play a game once more: ")
            if p == "Yes":
                Want_To_Play = True
            elif p == "No":
                Want_To_Play = False
        elif b == "Rock" and a == "Scissors":
            print(w)
            p = input("Do you want to play a game once more:")
            if p == "Yes":
                Want_To_Play = True
            elif p == "No":
                Want_To_Play = False
        elif b == "Paper" and a == "Scissors":
            print(l)
            p = input("Do you want to play a game once more: ")
            if p == "Yes":
                Want_To_Play = True
            elif p == "No":
                Want_To_Play = False
        elif b == "Paper" and a == "Rock":
            print(w)
            p = input("Do you want to play a game once more: ")
            if p == "Yes":
                Want_To_Play = True
            elif p == "No":
                Want_To_Play = False
        elif b == "Scissors" and a == "Rock":
            print(l)
            p = input("Do you want to play a game once more: ")
            if p == "Yes":
                Want_To_Play = True
            elif p == "No":
                Want_To_Play = False
        elif b == "Scissors" and a == "Paper":
            print(w)
            p = input("Do you want to play a game once more: ")
            if p == "Yes":
                Want_To_Play = True
            elif p == "No":
                Want_To_Play = False

play()



