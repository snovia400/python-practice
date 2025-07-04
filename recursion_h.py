#  Easy (1–5): Understand the Basics
# Print numbers from n to 1 using recursion.

# Print numbers from 1 to n using recursion.

# Find the sum of first n natural numbers using recursion.

# Find the factorial of a number using recursion.

# Calculate the power of a number a^b using recursion.



def count(n):
    if n == 1:
        print(1)
    else:
        count(n-1)
        print(n)
count(5)

def countdown(n):
    if n == 1:
       print(1)
    else:
        print(n)
        countdown(n-1)
countdown(5)


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


def sum(n):
    if n == 1:           #0,1,1,2,3,5
                         #0 1 2 3 4 5
        return 1
    else:
        return n + sum(n-1)
print(sum(2))


def power(n,p):
    if p == 0 :
        return 1
    else:
        return n* power(n,p-1)
print(power(2,3))

# Medium (6–10): Patterns & Decisions
# Reverse a string using recursion.

# Check if a string is a palindrome using recursion.

# Count digits in a number using recursion.

# Sum of digits of a number using recursion.

# Find the nth Fibonacci number using recursion








def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

print(fib(8))  


#recursion has beeen put to hold