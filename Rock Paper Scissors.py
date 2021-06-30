import random
import time

try:

    # choice = input("s for scissor, r for rock and p for paper")
    round = 10
    pplayer = 0
    pcomp = 0
    while True:
        while round != 0:
            sets = {"r": "Rock", "p": "Paper", "s": "Scissor"}
            print(f"You have {round} rounds")
            print("Enter s for scissor, r for rock and p for paper")
            indict = input()
            player = sets[indict]
            list1 = ["Rock","Paper","Scissor"]
            computer = random.choice(list1)
            print(f"Computer is thinking...")
            time.sleep(2)
            print(f"You selected {player} and Computer selected {computer}")
            if computer is "Rock":
                if player is "Paper":
                    print("Player won")
                    pplayer+=1
                elif player is "Scissor":
                    print("Computer Won")
                    pcomp+=1
                else:
                    print("Tie")
            elif computer is "Paper":
                if player is "Scissor":
                    print("Player won")
                    pplayer += 1
                elif player is "Rock":
                    print("Computer Won")
                    pcomp += 1
                else:
                    print("Tie")
            elif computer is "Scissor":
                if player is "Rock":
                    print("Player won")
                    pplayer += 1
                elif player is "Paper":
                    print("Computer Won")
                    pcomp += 1
                else:
                    print("Tie")

            round -= 1
            print(f"Player : {pplayer} and Comp : {pcomp}")

        if (pplayer > pcomp):
            print(f"Player Winner")
        elif (pplayer < pcomp):
            print(f"Computer Winner")
        else:
            print("Both Winners")

        playagain = input("Do you wanna play again?Y/N\n")
        if playagain.upper() == "Y":
            round = 10
            pplayer = 0
            pcomp = 0
        elif playagain.upper() == "N":
            print("Thanks for playing")
            break
        else:
            print("Invalid input")
            continue

except Exception as e:
    print("Wrong input")