# Easy (1–3): Basic Try-Except
# Zero Division
# Ask the user to enter two numbers and divide them. Handle division by zero using try-except.

# Type Conversion Error
# Ask for a number input. Try converting it to int and handle the error if input is not a number.

# File Not Found
# Try to open a file called data.txt in read mode. Handle the case where the file does not exist.


n1 = int(input('enter number 1: '))
n2 = int(input('enter number 2: '))

try:
    print(n1/n2)
except ZeroDivisionError:
    print('cannot be divided by zero')



n =  input('input a number: ')

try:
    int(n)
except ValueError:
    print('please enter an integer')

    

try:
    with open('data.txt','r') as f:
        f.read()
except FileNotFoundError:
    print('file not found')



# Medium (4–6): Multiple Exceptions & Else/Finally
# Multiple Exceptions
# Take two inputs from user. Convert them to integers and divide. Handle both ValueError and ZeroDivisionError.

# Use Else
# Ask user for a number. Use try-except-else to print the square only if there's no error.

# Use Finally
# Try opening a file and reading it. Use finally to print "Operation complete" no matter what.

n1 = (input('enter number 1: '))
n2 = (input('enter number 2: '))

try:
    n1 = int(n1)
    n2 = int(n2)
    print(n1/n2)
except ZeroDivisionError :
    print('cannot be divided by zero')
except ValueError:
    print('please enter integers')




try:
  n =  input('input a number: ')
  n = int(n)
except ValueError:
    print('enter integer')
else:
    print(n**2)


try:
    with open('fruits.txt' , 'r') as f:
        f.read()
except FileNotFoundError:
    print('not found')
finally:
    print('complete')

# Challenging (7–9): Practical Use Cases
# Safe List Access
# Have a list of 3 items. Ask the user for an index and print the item. Handle IndexError.

# Dictionary Key Access
# Have a dictionary of fruits and prices. Ask user for a fruit name. Handle missing key with KeyError.

# Custom Error Message
# Ask for age as input. If input is not a valid integer or below 0, show custom message: "Invalid age entered."

l = ['apple','banana','mango']

try:
    i = int(input('enter index'))
    print(l[i])
except IndexError:
    print('please enter appropriate index')
except ValueError:
    print('please enter interger')


fruits = {
    'apple' : 8,
    'banana' : 5,
    'orange' : 4
}
try:
    f = input('enter a fruit')
    print(fruits[f])
except KeyError:
    print('fruit not found!')

try:
    a = int(input('Enter your age: '))
    if a < 0:
        raise ValueError('❌ Invalid age: must be 0 or above.')
    print("✅ Your age is:", a)
except ValueError as e:
    print("Error:", e)

