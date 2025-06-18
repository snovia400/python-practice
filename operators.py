# Easy (1–6)
# Focus: Arithmetic, Comparison, Assignment

#PROBLEM 1 
# Add Two Numbers
# Ask the user for two numbers. Print their sum.


#PROBLEM 2
# Even or Odd
# Input a number and check if it’s even or odd using % (modulo).


#PROBLEM 3
# Swap Two Numbers Using Assignment Operators
# Swap two variables (without a third one) using Python assignment.


#PROBLEM 4
# Check if a Number is Positive, Negative, or Zero
# Use if, elif, and comparison operators.


#PROBLEM 5
# Check if Two Numbers are Equal
# Input two numbers and print True if equal, else False.


#PROBLEM 6
# Find the Largest of Three Numbers
# Use comparison operators and if-elif-else.


#PROBLEM 1 
n1  = int(input('enetr n1: '))
n2  = int(input('enetr n2: '))
result = n1  + n2
print(result)


# PROBLEM 2
num  = int(input('enter : '))
if num % 2 == 0:
    print('number is even')
else:
    print('number is odd')

#PROBLEM 3
a = 7
b = 5
a , b = b , a
print(f"the value of a is {a} and the value of b is{b}")

#PROBLEM 4
num1  = int(input('enter a number: '))
if num1 == 0:
    print('number is zero')
elif num1 < 0 : 
    print('number is negative')
else:
    print('number is positive')

#PROBLEM 5
n3  = int(input('enetr n1: '))
n4  = int(input('enetr n2: '))
print(f'{n3 == n4} {n3} and {n4}')


#PROBLEM 6
no1  = int(input('enetr n1: '))
no2  = int(input('enetr n2: '))
no3 = int(input('enetr n3: '))

if no1 > no2 and no1 > no3:
    print(f'{no1} is the greatest')
elif no2 > no1 and no2 > no3:
    print(f'{no2} is the greatest')
elif no3 > no1 and no3 > no2:
    print(f'{no3} is the greatest')
else:
    print('all are equal')
 


# Medium (7–12)
# Focus: Logical, Compound Assignment, Membership, Identity

# PROBLEM 7
# Is a Character a Vowel?
# Ask the user for a letter. Check if it is in 'aeiouAEIOU' using in.


#PROBLEM  8 
# Simple Login Check
# Ask for a username and password. If both match, print “Welcome”. Use and.


#PROBLEM 9 
# Score Modifier with Assignment Operators
# If score > 90, add 10 to score using +=. Otherwise, subtract 5 using -=.


#PROBLEM 10   
# Check if a Number is in Range (10–100)
# Use and to check if a number is between 10 and 100 (inclusive).


#PROBLEM  11 
# Compare Identity vs Equality

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)   # True?
# print(a is b)   # True or False?
# Write your own explanation.


#PROBLEM 12    
# Guessing Game: Check Membership
# You have a list of secret numbers [3, 7, 9]. Ask the user to guess a number. Check using in.


# PROBLEM 7
letter = input('enter a letter: ')
if letter.lower() in 'aeiou':
    print('letter is a vowel')
else:
    print('letter is not a vowel')

#PROBLEM 8

user_set = input('enter your username: ')
pass_set = input('enter your password: ')

con_user = input('confirm your user: ')
con_pass = input('confirm your password: ')

if con_user == user_set and con_pass == pass_set:
    print('welcome!')
else:
    print('incorrect user or password') 

#PROBLEM 9
sc = int(input('enetr your score: '))
if sc > 90:
    sc += 10
else:
    sc -= 5
print(sc)
#PROBLEM 10
range = int(input('enter a number: '))
if range >= 10 and range <= 100:
    print('number is between 10 and 100')
else:
    print('number is out of range')

#PROBLEM 11
# a==b will be true because their value is same. they are equal.
# a is b will be false because a is different,their identity is different

# PROBLEM 12
sec = [3, 7, 9]
guess = int(input('enter your guess: '))
if guess in sec:
    print('congrats you\'ve guessed the number!')
else:
    print('you failed stupid')


# Hard (13–16)
# Focus: Logical puzzles, Nested Conditions, Chained Comparisons

#PROBLEM 13
# Pass or Fail with Multiple Conditions
# Input marks for 3 subjects. Pass if all are >= 33 and average is >= 40.

#PROBLEM 14
# Check if Number is a Multiple of Both 3 and 5
# Use and with modulo operator: if num % 3 == 0 and num % 5 == 0.

#PROBLEM 15
# Chained Comparison Puzzle
# Predict and explain:

# x = 5
# print(3 < x < 10)   # ?
# print(3 < x > 10)   # ?

#PROBLEM 16
# Graduation Eligibility Checker
# Variables:

# credits = 130
# GPA = 3.6
# has_fail = False
# Check if student can graduate:

# Credits ≥ 120 or GPA > 3.5

# AND has_fail is False



#PROBLEM 13
eng , math , sci = int(input('enter marks of eng')) ,int(input('enter marks of math')) ,int(input('enter marks of sci'))
avg  = (eng + math + sci)/3
if eng >= 33 and math >= 33 and sci >= 33 and avg >= 40 :
    print('you have passed')
else:
    print('you failed')

#PROBLEM 14
num10 = int(input('enter ur number: '))

if num10 % 3 == 0 and num10 % 5 == 0:
    print(True)
else:
    print(False)

#PROBLEM 15
#the first one will be true as 3 is less than 5 and 5 is less than 10
# the second one will be false as 3 is less than 5 but 5 is not greater than 10


#PROBLEM 16
gpa = 3.6
credits  = 130 
fail = False
if (gpa > 3.6 or gpa > 120) and not fail :
    print('u can graduate')
else:

    print('u cannot graduate')














