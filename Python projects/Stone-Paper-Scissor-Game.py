import random
'''
1 for stone
-1 for paper
0 for scissor
'''
computer = random.choice([-1, 0,1])
youstr = input("Enter your choice: ")
youDict = {'s': 1, 'p': -1, 'c': 0}
reverseDict = {1: 'Stone', -1: 'Paper', 0: 'Scissor'}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if you == computer:
    print("It's a draw!")

else:
    if computer == -1 and you == 1:
        print("You Lose!")
    elif computer == -1 and you == 0:
        print("You Win!")
    elif computer == 1 and you == -1:
        print("You Win!")
    elif computer == 1 and you == 0:
        print("You Lose!")
    elif computer == 0 and you == -1:
        print("You Lose!")
    elif computer == 0 and you == 1:
        print("You Win!")
    else:
        print("Something went wrong")


