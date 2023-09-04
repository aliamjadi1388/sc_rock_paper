player1Name = input("please enter your name p1: ")
player2Name = input("please enter your name p2: ")

scoreP1 = 0
scoreP2 = 0

countPlay = int(input("enter count play ? "))
for i in range(1,countPlay+1):
    player1 = input(f"please enter sc or rock or paper {i}: ")
    player2 = input(f"please enter sc or rock or paper {i}: ")
    if player1 == player2:
        print("draw")
    elif player1 == "rock" and player2 == "sc":
        print(f"{player1Name}  win")
        scoreP1 += 1
    elif player1 == "rock" and player2 == "paper":
        print(f"{player2Name}  win")
        scoreP1 += 1
    elif player1 == "sc" and player2 == "rock":
        print(f"{player2Name}  win")
        scoreP1 += 1    
    elif player2 == "sc" and player2 == "paper":
        print(f"{player2Name}  win")   
    elif player2 == "paper" and player2 == "rock":
        print(f"{player2Name}  win")       
    elif player2 == "paper" and player2 == "sc":
        print(f"{player2Name}  win")      

if scoreP1 == scoreP2:
    print("draw")
elif scoreP1>scoreP2:
    print(f"{player1} win")    
elif scoreP1<scoreP2:
    print(f"{player2} win")             