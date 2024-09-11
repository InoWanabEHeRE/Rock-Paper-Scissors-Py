import random

print("""Welcome to Rock Paper Scissors!
In this game, you will go against the computer in a game of rock paper scissors.
When prompted, please answer in one word.
Do not capitalize or punctuate.
Enjoy!
""")
while True:
    userin = input("What's your move? ")
    compin = random.randint(1, 3)
    if compin == 1:
        print("The computer chose Rock")
    elif compin == 2:
        print("The computer chose Paper")
    elif compin == 3:
        print("""
The computer chose Scissors""")

    if userin == "rock":
        userin = 1
    elif userin == "paper":
        userin = 2
    elif userin == "scissors":
        userin == 3
    else:
        print("User error")

    if compin == userin:
        print("Tie")
        continue
    elif compin == 1 and userin == 2:
        print("You won!")
    elif compin == 1 and userin == 3:
        print("You lost")
    elif compin == 2 and userin == 1:
        print("You lost")
    elif compin == 2 and userin == 3:
        print("You won!")
    elif compin == 3 and userin == 1:
        print("You won!")
    elif compin == 3 and userin == 2:
        print("You lost")
    if str(input("""
Do you want to play another game, yes or no?\n""")) == 'yes':
            continue
    else:
        break
