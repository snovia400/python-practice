# Easy (1–5): Basics
# ✅ Create a simple generator that yields numbers from 1 to 5.

# ✅ Create a generator that yields squares of numbers from 1 to n.

# ✅ Create a generator to yield characters from a string one by one.

# ✅ Write a decorator that prints "Function started" before any function runs.

# ✅ Write a decorator to print the function’s name before it executes.


def to5(n):
    for i in range (1,n+1):
        yield i

for num in to5(5):
    print(num)


def sq(n):
    for i in range(1,n+1):
        yield i**2

for num in sq(5):
    print(num)



def string(s):
    for i in s:
        yield i
for chr in string('helllllllo'):
    print(chr)



def start(func):
    def wrap():
        print('started')
        func()
        print('ended')
    return wrap
@start
def mid():
    print('running')
mid()

def nam(func):
    def wrap():
        print(func.__name__)
        func()
    return wrap
@nam
def greeet():
    print('hiii')

greeet()       


# 📗 Medium (6–10): Real Use Cases
# ✅ Create a generator to yield even numbers up to n.

# ✅ Write a generator to yield Fibonacci numbers up to n.

# ✅ Write a decorator that measures execution time of a function.

# ✅ Create a decorator that only allows a function to run if a condition (like age > 18) is met.





def even(n):
    for i in range(1,n+1):
        if i % 2 == 0:
            yield i

for evens in even(10) :
    print(evens)






def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
    

for fibo in fib(5):
    print(fibo)

import time

def timee(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'the execution time is {end - start}')
    return wrapper
@timee
def slow():
    for i in range(1,10):
        print(i)
    
slow()



def allow(func):
    age = int(input('enter ur age: '))
    def wrapper():
        if age >= 18:
            func()
        else:
         print('sorry')
    return wrapper
@allow
def valid():
    print('ur age is valid')

valid()







