import random

def welcome():
    for i in range (0,10):
        print("*","\t",end="")
    print()
    print("*",end="")
    for i in range (0,3):
        print("\t",end="")
    print("QUARANTINE","\t",end="")
    for i in range (0,3):
        print("\t",end="")
    print("*")
    for i in range (0,10):
        print("*","\t",end="")
    print()
    for i in range (0,10):
        print("*","\t",end="")
    print()
    print("*",end="")
    for i in range (0,4):
        print("\t",end="")
    print("AND","\t",end="")
    for i in range (0,3):
        print("\t",end="")
    print("*")
    for i in range (0,10):
        print("*","\t",end="")
    print()
    for i in range (0,10):
        print("*","\t",end="")
    print()
    print("*",end="")
    for i in range (0,4):
        print("\t",end="")
    print("CODE","\t",end="")
    for i in range (0,3):
        print("\t",end="")
    print("*")
    for i in range (0,10):
        print("*","\t",end="")
    print()
    input("\n\tPRESS ANY KEY TO START:")

def mainmenu ():
    print("\n" * 100)
    print("ROCK, PAPER, SCISSORS")
    print("1.PLAY\n2.RULES\n3.EXIT")
    ch=int(input("ENTER YOUR CHOICE:"))
    if ch == 1:
        rockpaperscissors()
    elif ch == 2:
        rockpaperscissorsrules()
    elif ch == 3:
        exit()

def rockpaperscissorsrules():
    print("\n" * 100)
    with open("/rps.txt","r") as file:
        s = file.read()
        print(s)
        file.close()
    input("\n\tPRESS ANY KEY TO GO TO MAINMENU:")
    mainmenu()

def rockpaperscissors():
    print("\n" * 100)
    print("WELCOME TO ROCK PAPER AND SCISSORS")
    print("You will be competing against the computer. The player that scores 5 points first, will be declared as the winner!")
    print("If your choice is Rock,please Enter 0")
    print("If your choice is Paper,please Enter 1")
    print("If your choice is Scissors,please Enter 2")
    print("If you wish to exit,please Enter -1")
    user = 0
    comp = 0
    cnt = 0
    chc = ["Rock", "Paper", "Scissors"]
    while ( user < 5 and comp < 5 and cnt < 25):
        cnt += 1
        u_ch = int(input("\nEnter your choice in numbers:"))
        if u_ch == -1:
            print("Thank you")
            return
        elif u_ch >= 3:
            print("INVALID")
            continue
        c_ch = random.choice([0, 1, 2])
        if u_ch == 0 and c_ch == 1:
            comp += 1
        elif u_ch == 0 and c_ch == 2:
            user += 1
        elif u_ch == 1 and c_ch == 0:
            user += 1
        elif u_ch == 1 and c_ch == 2:
            comp += 1
        elif u_ch == 2 and c_ch == 0:
            comp += 1
        elif u_ch == 2 and c_ch == 1:
            user += 1
        print("You:", chc[u_ch])
        print("Computer:", chc[c_ch])
        print("Your score:", user, "\t Computer's Score:", comp)
    if (user > comp):
        print("Congragulations!You win!")
    elif (comp > user):
        print("Oops!Sorry you lose. Better luck next time!")
    else:
        print("Match Draw")
    input("\nPRESS ANY KEY TO GO TO MAINMENU:")
    mainmenu()

welcome()
mainmenu()






