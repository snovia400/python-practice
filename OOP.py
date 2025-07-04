# Easy (1–7): Class Basics
# Create a class Car with attributes brand and model. Create an object and print its attributes.

# Add a method start() in the Car class that prints "Car started".

# Create a class Student with attributes name and age, and a method greet() that says hello with their name.

# Use __init__ to automatically set values when creating an object.

# Add a method is_adult() in Student that returns True if age >= 18.

# Create two Student objects and compare their ages.

# Add a grade attribute to Student and a method to check if the student passed (grade ≥ 60).




class car:
    brand = 'toyota'
    model = 'idk'
    def start():
        print('started')

car1 = car
print('brand',car1.brand,'model',car1.model)
car1.start()


class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age 
        self.grade = grade
    def greet(self):
        print('hello',self.name,'ur age is',self.age)
    def adult(self):
        print(self.age >= 18)
    def passed(self):
        if self.grade > 60:
            print('passed')
        else:
            print('failed')
    def compare(anna,ben):
        if ben.age == anna.age:
            print('equal')
        else:
            print('not equal')


anna = student('anna',19,70)
print(anna.name)
anna.greet()
anna.adult()
anna.passed()
ben = student('ben',20,13)
ben.passed()

if ben.age > anna.age:
    print('ben is older')
elif anna.age > ben.age:
    print('anna is older')
else:
    print('both are of same age')


# Medium (8–14): Encapsulation & Multiple Objects
# Create a BankAccount class with methods deposit() and withdraw(), and a private balance.

# Add a method check_balance() to return the current balance.

# Prevent the balance from going below 0 on withdraw().

# Create a Book class with title, author, and year. Add a method to print all info.

# Create a Library class that contains a list of Book objects and a method to display all books.

# Add a method to Library to search for a book by title.

# Add a method to remove a book from the library list.


class bankaccount:
    def __init__(self,balance):
       self.balance = balance
    def deposite(self,n):
        self.balance+=n
    def withdraw(self,n):
        if n > self.balance:
            print('insufficient funds')
        else:
            self.balance -= n
    def check_balance(self):
        print( self.balance)

snovia = bankaccount(0)
snovia.deposite(100)
snovia.check_balance()
snovia.withdraw(5)
snovia.check_balance()
snovia.withdraw(44)
snovia.check_balance()





#
class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f'{self.title} by {self.author}')


b1 = book('To Kill a Mockingbird', 'Harper Lee')
b2 = book('snovia', 'snovia')


class library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def display(self):
        for book in self.books:
            book.info()

    def search(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print('Found!')
                book.info()
                return
        print('Not found!')  
    def remove(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Removed '{title}'")
                return
        print("Book not found to remove.")  


lib = library()
lib.add(b1)
lib.add(b2)

lib.display()
lib.search('tO kill a mockingbird')
lib.remove('snovia')




