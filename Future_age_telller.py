//This program tells your future age in whichever year you want!
def age_teller():
    print(f"your cuurent age is {current_year - dateofb}yrs")

def century_teller():
    print(f"you will be 100yr old in {dateofb+100}")

def future_age():
    fyr=int(input("enter the yr in which you want to know your age"))
    fage=fyr-dateofb
    print(f"you will be {fage}yr old in {fyr}")

if __name__ == '__main__':
    agetell = input("enter a to know yourage ,b to know your age in future yr , c to know your golden jubbly yr\n")
    dateofb = int(input("enter your DOB year here\n"))
    current_year = int(input("enter current year here\n"))
    if dateofb > current_year:
        print("you are yet to born. please wait for 9 months")
    elif dateofb < 1800:
        print("you are god")
    else:
        agetel=agetell.casefold()
        if agetel=="a":
            age_teller()
        elif agetel=="b":
            future_age()
        elif agetel=="c":
            century_teller()
        else:print("you gave wrong input.please try again")
