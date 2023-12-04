import random
options = ['rock', 'paper', 'scissors']
player1 = input('Please enter your name:\n')
player2 = "Computer"
p1_opt = input("rock, paper, scissors?\n")
p2_opt = random.choice(options)
flag = 0
while(flag==0):
    if p1_opt == p2_opt:
        flag = 1
    elif p1_opt == 'rock':
        if p2_opt == 'paper':
            print("Paper beats rock. %s wins"%player2)
            flag = 1
        elif p2_opt == 'scissors':
            print("Rock beats scissors. %s wins"%player1)
            flag = 1
    elif p1_opt == 'scissors':
        if p2_opt == 'paper':
            print("Scissors beats paper. %s wins"%player2)
            flag = 1
        elif p2_opt == 'rock':
            print("Rock beats scissors. %s wins"%player1)
            flag = 1
    elif p1_opt == 'paper':
        if p2_opt == 'rock':
            print("Paper beats rock. %s wins"%player1)
            flag = 1
        elif p2_opt == 'scissors':
            print("Scissors beats rock. %s wins"%player2)
            flag = 1
else:
        print("Quitting.")
