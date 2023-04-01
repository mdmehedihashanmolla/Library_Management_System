Students_Username = ['Mehedi', 'Arnab', 'Torsha', 'Prakash']
Students_Id = ['1234', '5678', '2134', '9876']
class Library: 
    def __init__(self):
        self.books = ['Algorithm', 'Data Structure', 'Python', 'Machine Learning','Deep Learning', 'Django', 'Html', 'Css', 'Javascript']

    def displayAvailableBooks(self):
        print("These Books Are Present in I.C.S.S Library :  ")
        for book in self.books:
            print("* " + book)

    def IssueingBooks(self, bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname} Book. Please keep it safe and return it within 15 days.")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry, Either this book is not available or has been issued by someone else. Please wait untill the book is return.")
            return False

    def returnBook(self, bookname):
            self.books.append(bookname)
            print("Thanks for returning/Adding this book! Hope you have enjoyed it !")
     

    def addNewBooks(self):
        F = open("Books_List.txt", "a+")
        Book = input("Enter The Books Name : ")
        F.write("* "+Book+"\n")
        F.close()
        F = open("Books_List.txt", 'r')
        print(F.read())
        F.close()


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ".strip())
        return self.book

    def rturn(self):
        self.book = input("Enter the name of the book you want to return: ".strip())
        return self.book


class Library_Menu(Library, Student):
    def __init__(self):
        Library.__init__(self)
        Student.__init__(self)

    def Main_menu(self):

        while(True):
            print("*********************************************")
            print("|**||   ********Main Menu*********      ||**|")
            print("|**||   Welcome To I.C.S.S Library      ||**|")
            print("|**||   Type '1' For All Book's List    ||**|")
            print("|**||   Type '2' For Issued a Book      ||**|")
            print("|**||   Type '3' For Return/Add The Book||**|")
            print("|**||   Type '4' For Add a New Book     ||**|")
            print("|**||   Type '5' For Exit               ||**|")
            print("*********************************************")

            Menu_Choice = (input("Enter Your Choice : ".strip()))
            if Menu_Choice == '1':
                self.displayAvailableBooks()
            elif Menu_Choice == '2':
                self.IssueingBooks(self.requestBook())
            elif Menu_Choice == '3':
                self.returnBook(self.rturn())
            elif Menu_Choice == '4':
                self.addNewBooks()
            elif Menu_Choice == '5':
                print("Thank You For Chooseing I.C.S.S Library")
                exit()
            else:
                print("Invalid Choice")

class Student_Login(Library_Menu):
    def __init__(self):
        Library_Menu.__init__(self)

    def Verify_Students_Username(self):
        Username = input("Enter Your Student Username : ".strip())
        if Username in Students_Username:
            index_no = Students_Username.index(Username)
            self.Verify_Students_ID(index_no)
        else:
            print("Wrong Username Try Again")

    def Verify_Students_ID(self,l):
     
         for i in range(1, 6, 1):
             Id = (input("Enter Your Student Id : "))
             if Id == Students_Id[l]:
                 self.Main_menu()
                 break
             else:
                 print("Wrong Id")
    
         print("You can't use Alphabet Here")
        

o = Student_Login()
o.Verify_Students_Username()
