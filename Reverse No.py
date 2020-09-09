def makepalindrome(pali):
    if pali<10:
        print(f"the number is itself palindrome i.e. {pali}")
    elif str(pali)==str(pali)[::-1]:
        print(f"the next palindrome is {pali}")
    else:
        pali2=pali+1
        makepalindrome(pali2)

if __name__ == "__main__":
    no_ip=int(input("enter the numbers you want to make palindrome\n"))
    for i in range(no_ip):
        pali=int(input("enter the numbers you want to palindrome\n"))
        makepalindrome(pali)

