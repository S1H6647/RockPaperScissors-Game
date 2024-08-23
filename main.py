'''
Rock = 0
Paper = 1
Scissors = -1
'''

import random

computer = random.choice([-1,0,1])
round = int(input("Enter how many rounds you want to play: "))
i = 1
while (i<=round):
    youString = input("Enter your choice: ")
    youDict = {
    "P":1,
    "S":-1,
    "R":0
    }
    reverseDict = {
    1:"Paper",
    -1:"Scissors",
    0:"Rock"
    }
    You = youDict[youString] # You is a numeric value

    print(f"You chose {reverseDict[You]} \t")
    print(f"Computer chose {reverseDict[computer]}")

    if(computer == You):
        print("It's a draw!")

    else:
        # Computer == 0 
        if(computer == 0 and You == 1):
            print("You Win!")
        elif(computer == 0 and You == -1):
            print("You Lose!")

        # Computer == 1
        if(computer == 1 and You == 0):
            print("You Lose!")
        elif(computer == 1 and You == -1):
            print("You Win!")

        # Computer == -1
        if(computer == -1 and You == 0):
            print("You Win!")
        elif(computer == -1 and You == 1):
            print("You Lose!")
    i+=1
