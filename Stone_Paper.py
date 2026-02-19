import random
cscore = 0
uscore = 0

print("Welcome to Stone Paper Scissors Game\n")

while True:
    print(f"Current Score: You- {uscore} Computer- {cscore}\n")

    user = int(input("Enter 1 for Stone, 2 for Paper and 3 for Scissors:\n "))
    comp = random.randint(1,3)

    if user == 1 and comp == 3:
        uscore +=1
        print("You Won this round\n")

    elif user == 2 and comp == 1:
        uscore +=1
        print("You Won this round\n")

    elif user == 3 and comp == 2:
        uscore +=1
        print("You Won this Round\n")

    elif user == comp:
        print("This Round is Draw\n")

    else:
        cscore +=1
        print("Computer Won this Round\n")

    if uscore == 5:
        print(f"Congratulations! You Won the Game with Scoreline {uscore} to {cscore}")
        break
    elif cscore == 5:
        print(f"Computer Won the Game with Scoreline {cscore} to {uscore}")
        break