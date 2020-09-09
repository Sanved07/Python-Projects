
def sequence1():
    number1 = int(input("enter the number\n"))
    i = 1
    while i <= number1:
        print("*" * i)
        i += 1
        continue


def sequence2():
    number2 = int(input("enter the number\n"))
    q = number2
    while q >= 1:
        print("*" * q)
        q -= 1
        continue

def play1():
    boolean = (input("enter the squence \n"))
    boolean = boolean.capitalize()
    if boolean == "Ascending":
        sequence1()
    if boolean == "Descending":
        sequence2()


def exit():
    print("you have successfully exited the program \n")


play2=str(input("press y to play and n to exit the program\n"))
if play2 =='y':
    play1()


elif play2=='n':
    exit()