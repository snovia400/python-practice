#  Beginner Level (1–5)
# Greet Me
# Write a function greet() that prints "Hello, world!".

# Add Two Numbers
# Write a function add(a, b) that prints the sum of a and b.

# Check Even or Odd
# Write a function is_even(n) that prints "Even" if the number is even, otherwise "Odd".

# Area of a Circle
# Write a function area(radius) that returns the area using π × r² (use π = 3.14).

# Max of Two
# Write a function max_of_two(a, b) that returns the larger number.



# PROBLEM 1
def greet():
    print('hello world')
greet()
# PROBLEM 2
def add(a,b):
    print(f'the sum of {a} and {b} is {a+b}')
add(5,5)
# PROBLEM 3
def even(n):
    if n % 2 == 0:
        print('even')
    else:
        print('odd')
even(9)
# PROBLEM 4
def area(r):
    r = r**2
    pie = 3.14
    print(f'the area of circle is: {r*pie}')
area(5)
# PROBLEM 5
def max_of_two(a, b):
    if a>b:
        print(f'{a} is the greatest ')
    else:
         print(f'{b} is the greatest ')

max_of_two(9,16)



# Medium Level (6–10)
# Factorial Finder
# Write a function factorial(n) that returns the factorial of n.

# Fibonacci Generator
# Write a function fibonacci(n) that prints the first n Fibonacci numbers.

# Sum of a List
# Write a function sum_list(lst) that returns the sum of all numbers in a list.

# Count Vowels
# Write a function count_vowels(s) that returns the number of vowels in a given string.  

# Reverse String
# Write a function reverse_string(s) that returns the reversed version of the string s. 


def fact(n):
   result = 1
   for i in range(1,n+1):
       result *= i
   print(result)

fact(5)

def fibonacci(n):
    a, b = 0, 1
    count = 0

    while count < n:
        print(a)
        a, b = b, a + b
        count += 1
fibonacci(7)
   
def sum_lst(lst):
    sum = 0
    for i in lst:
        sum += i
    print(sum)

sum_lst([1,2,3])

def vowels(s):
    count = 0
    for i in s:
        if i.lower() in 'aeiou':
           count += 1
    return count
print(vowels('helloooo'))


def rev(s):
    rev = s[::-1]
    return rev
print(rev('helloooo'))

# Challenging Level (11–15)
# Check Prime
# Write a function is_prime(n) that returns True if the number is prime, else False.

# Palindromic Word
# Write a function is_palindrome(word) that checks if a word reads the same backward.

# Power Calculator
# Write a function power(base, exponent) that returns base raised to exponent.

# Custom Greet
# Write a function greet_user(name, age) that prints:
# "Hello [name], you are [age] years old!"

# Find Largest in List
# Write a function find_max(lst) that returns the largest number from a list.


def prime(n):
    if n<2:
        return False
    for i in range (2,n):
        if n%i == 0:
            return False
        return True
    
print(prime(6))


def pal(w):
    rever = w[::-1]
    if rever == w:
        return 'palindromic'
    return 'not palindromic'
print(pal('121'))


def pow(b,e):
    return b ** e

print(pow(2,2))


def greet(n,a):
    return (f'hello {n} , you are {a} years old')

name = input('enter ur name')
age = input('enter ur age')

print(greet(name,age))


def max(l):
    max = 0
    for i in l:
        if i > max:
            max = i
    return max
print(max([1,2,3,88,44,66]))


