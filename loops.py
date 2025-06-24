
# 🔹 Easy (1–7) — Basics & counting


#PROBLEM 1
# Print numbers 1 to 10 using a for loop.


#PROBLEM 2
# Print numbers 10 to 1 using a while loop.


#PROBLEM 3
# Print all even numbers between 1 and 20.


#PROBLEM 4
# Print the sum of numbers from 1 to 100.


#PROBLEM 5
# Print the first 10 multiples of a number (input by user).


#PROBLEM 6
# Count how many numbers between 1–50 are divisible by 7.


#PROBLEM 7
# Take 5 inputs from user using a loop and print their total.



# PROBLEM 1
for i in range (1,11):
     print(i)

#PROBLEM 2
b = 10
while b>=1:
    print(b)
    b -=1

#PROBLEM 3
for i in range(1,21):
    if i % 2 == 0:
        print (i)

#PROBLEM 4
total = 0
for i in range (1,101):
   total += i

print(total)

# PROBLEM 5

n = int(input('enter a number: '))
for i in range(1,11):
   
   print(n*i)

#PROBLEM 6
div7 = 0
for i in range(1,51):
    if i%7 == 0:
        div7 +=1
print(div7)

#PROBLEM 7

c =1
t = 0
while c < 6:
   d= int(input('enter a number: '))
   t+= d
   c+=1
print(f'the total is {t}')

# 🔸 Medium (8–14) — Logic + loop control

#PROBLEM 8
# Print the factorial of a number.


#PROBLEM 9
# Use a while loop to reverse a number (e.g., 123 → 321).


#PROBLEM 10
# Print each character in a string using a loop.


#PROBLEM 11
# Count vowels in a given string.


#PROBLEM 12
# Print a pattern:


# *
# * *
# * * *
# * * * *

# PROBLEM 13
# Take input until user types “exit”. Count how many inputs were taken.


#PROBLEM 14
# Loop through a list of numbers and print the largest one.




#PROBLEM 8
num = int(input('enter a number: '))
fact = 1
for i in range (1,num+1):
    fact *= i
print(fact)


#PROBLEM 9
'''
DIFFICULT
'''

#PROBLEM 10
strin = input('enter a string:')
for i in strin:
    print(i)

#PROBLEM 11
count =0
for i in strin:
    if i.lower() in 'aeiou':
        count +=1
print(count)

#PROBLEM 12
strs = int(input('enter the no of strs'))
for i in range (1,strs+1):
    print('*'*i)

#PROBLEM 13
inpcnt = 0
inputt = ''
while inputt != 'exit':
  inputt=input('enter')
  if inputt == 'exit':
    break
  inpcnt+=1

print(inpcnt)


#PROBLEM 14
lis  =[]
for i in range (1,4):
    g  = int(input('enter number: '))
    lis.append(g)
largest = 0
for n in lis:
    if n>largest:
        largest = n
print (f'the list is {lis} and the largest number is {largest}')

# 🔺 Challenging (15–20) — Pattern & logic stretch

# PROBLEM 15
# Print Fibonacci series up to N terms.


#PROBLEM 16
# Print this pattern:

# 1
# 2 3
# 4 5 6
# 7 8 9 10

#PROBLEM 17
# Use nested loops to print multiplication tables from 1 to 5.


#PROBLEM 18
# Find the sum of digits of a number (e.g., 423 → 4+2+3 = 9).


#PROBLEM 19
# Print a triangle of numbers for user input rows:


# Input: 4
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# PROBLEM 20
# Loop through numbers 1–30 and:

# Print “Fizz” if divisible by 3

# Print “Buzz” if divisible by 5

# Print “FizzBuzz” if divisible by both


#PROBLEM 15





