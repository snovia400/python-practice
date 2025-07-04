# Easy (1–5): Basic Inheritance
# Create a class Animal with a method sound(). Create a subclass Dog that overrides sound() to print "Bark".

# Create a class Person with name and age. Inherit a Student class from it that also has a grade.

# Make a Vehicle class with method move(). Inherit Car and Bike from it, and override move() in each.

# Add a __str__() method in the Student class to print student info cleanly.

# In the Person class, make a method is_adult() that returns True if age ≥ 18. Use it from Student.

class animal:
    def sound():
        print('sound')


class dog(animal):
    def sound():
        print('woof woof')


a =animal
a.sound()

dog = dog
dog.sound()

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(self.name, self.age)
    def adult(self):
        
        return self.age > 18

class stud(person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  
        self.grade = grade
        # print(self.grade)

    def __str__(self):
        return f'name:{self.name} age:{self.age} grade:{self.grade}'
    
    def adult_check(self):
        if not super().adult():
            print('minor')
        else:
            print('mature')

s1 = stud('ashley',19,98)
print(s1)

s1.adult_check()



class vehicle:
    def move():
        print('move')

class car(vehicle):
    def move():
        print('broom')


class bike(vehicle):
    def move():
        print('zroom')

car1 = car
car1.move()

bike1 = bike
bike.move()

unknown = vehicle
vehicle.move()

# Medium (6–10): super() and method chaining
# Use super() in Student.__init__() to call Person.__init__() instead of repeating code.

# Create a Shape class with method area(). Inherit Rectangle and Circle from it. Override area() in each.

# Make a BankAccount class with balance. Inherit a SavingsAccount that has interest_rate and method to calculate interest.

# Create a Book class. Then inherit EBook class that also has file_size.

# Create an Employee class with salary. Make a subclass Manager that adds department. Use super() in __init__().


class shape:
    
    def area(self):
        return 'area'
class circle(shape):
    def area(self,r):
        self.r = r
        return 3.14*self.r*self.r
    
s = circle()
print(s.area(3))

class rect(shape):
    def area(self,l,w):
        self.l = l
        self.w = w
        return l*w
d = rect()
print(d.area(4,3))


class bank:
    def __init__(self,principle,rate,time):
        self.principle = principle
        self.rate = rate
        self.time = time
    
class saving(bank):
   def interest(self):
     self.inter = (self.principle * self.rate * self.time)/100
     return self.principle + self.inter

f = saving(5000,10,1)
print(f.interest())


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):  # Inheriting from Book
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call Book's constructor
        self.file_size = file_size


ebook1 = EBook("Digital Fortress", "Dan Brown", 5.6)


print(ebook1.title)        
print(ebook1.author)       
print(ebook1.file_size)    



class employee:
  def __init__(self,salary):
      self.salary =salary


class manager(employee):
    def __init__(self,d,salary):
      super().__init__(salary)
      self.d = d

snovia = manager('marketing',10000)
print(snovia.d,snovia.salary)


































