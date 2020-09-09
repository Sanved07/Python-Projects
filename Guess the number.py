import random
n=random.randint
nguess=0
print("welcome to the game ! you have 9 chances to guess the number.")
while(nguess<9):
    no_guess = int(input("guess the number\n"))
    if no_guess > n:
        print("you entered greater number. Plz enter smaller number")
        nguess += 1
        print(f"{9 - nguess} chances left")
    elif no_guess < n:
        print("you entered smaller number. Plz enter greater number")
        nguess += 1
        print(f"\n{9 - nguess} chances left")
    elif no_guess == n:
        print("You won the game")
        break
else :
    print("Game Over !")


