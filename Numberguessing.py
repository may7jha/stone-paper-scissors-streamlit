import random

num = random.randint(1,100)

tries = 0

while True:
    guessed = int(input("guess a number Between 1 to 100:"))
    tries += 1
    if guessed == num:
        print(f" Congratulations! You guessed the number in {tries} tries")
        break
    elif guessed > num:
        print(" You need to go lower\n")
    elif guessed < num:
        print(" You need to go higher\n ")



    