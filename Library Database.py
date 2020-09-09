class Library:
    def __init__(self,booklist,library):
        self.booklist=booklist
        self.liname=library
        self.lendict={}

    def display(self):
        print("we have following books in our library")
        for book in enumerate(self.booklist):
            print(book)

    def lendbook(self,user,book):
        if book not in sanved.booklist:
            print("you enetered wrong book name")
            exit()
        elif book not in self.lendict.keys():
            self.lendict.update({book:user})
            print(f"{book} owned by {user}")

        else:print(f"the book is already owned by {self.lendict[book]}")


    def addbook(self,book):
        self.booklist.append(book)
        print(f"your {book} book has been added")

    def returnn(self,book):
        self.lendict.pop(book)
        print(f"your {book} has been returned successfully")

if __name__ == '__main__':
    sanved=Library(["harry potter","rich dad poor dad","power of your subconcious mind"],"SANVED'S")
    print(f"welvome to {sanved.liname}library")
    while(True):
        option=int(input("1 to display book; "
                     "2 to lend book; "
                     "3 to add book; "
                     "4 to return book; "
                         "5 to exit code; \n"))
        if option==1:
            sanved.display()
            continue
        elif option==2:
            user2=input("enter the user name\n")
            book2=input("enter to book you want to lend\n")
            sanved.lendbook(user2.casefold(),book2.casefold())
            continue
        elif option==3:
            adder=input("enter the name of the book you want to add \n ")
            sanved.addbook(adder)
            continue
        elif option==4:
            retu1=input("enter the name of book you want to return \n")
            sanved.returnn(retu1)
            continue
        elif option==5:
            exit()
        else:print("wrong input")
        break

