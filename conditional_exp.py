# PROBLEM 1  
# Grade Based on Marks  
marks = int(input('Enter your marks: '))  
if marks >= 90:  
    print('A+')  
elif marks >= 80 and marks <= 89:  
    print('B')  
elif marks >= 70 and marks <= 79:  
    print('C')  
else:  
    print('Fail')  


# PROBLEM 2  
# Number Range Classification  
num = int(input('Enter your number: '))  
if 10 <= num <= 50:  
    print('Your number is between 10 and 50')  
elif 51 <= num <= 100:  
    print('Your number is between 51 and 100')  
elif num > 100:  
    print('Your number is above 100')  
else:  
    print('Number is below 10')  


# PROBLEM 3  
# Greatest of Three + Equality Check  
no1 = int(input('Enter n1: '))  
no2 = int(input('Enter n2: '))  
no3 = int(input('Enter n3: '))  
two_equals = 0  

if no1 > no2 and no1 > no3:  
    print(f'{no1} is the greatest')  
if no1 == no2 or no1 == no3:  
    two_equals += 1  
if no2 > no1 and no2 > no3:  
    print(f'{no2} is the greatest')  
if no2 == no1 or no2 == no3:  
    two_equals += 1  
if no3 > no1 and no3 > no2:  
    print(f'{no3} is the greatest')  
if no3 == no2 or no3 == no1:  
    two_equals += 1  
if two_equals == 3:  
    print('All are equal')  
if two_equals == 2:  
    print('2 are equal')  


# PROBLEM 4  
# Traffic Light Color Meaning  
clr = input('Enter your colour: ')  
if clr == 'red':  
    print('Stop')  
elif clr == 'yellow':  
    print('Wait')  
elif clr == 'green':  
    print('Go')  
else:  
    print('Invalid')  


# PROBLEM 5  
# Leap Year Checker  
year = int(input('Enter your year: '))  
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  
    print('Year is leap')  
else:  
    print('Year is not leap')  


# PROBLEM 8  
# Positive/Negative and Even/Odd  
numb = int(input('Enter a number: '))  
if numb == 0:  
    result = 'zero'  
elif numb < 0:  
    result = 'negative'  
else:  
    result = 'positive'  

if numb % 2 == 0:  
    result2 = 'even'  
else:  
    result2 = 'odd'  

print(f'The number is {result} and {result2}')  


# PROBLEM 9  
# Day of the Week from Number  
days = {  
    1: 'Monday',  
    2: 'Tuesday',  
    3: 'Wednesday',  
    4: 'Thursday',  
    5: 'Friday',  
    6: 'Saturday',  
    7: 'Sunday'  
}  
numbe = int(input('Enter the number of the day: '))  
if numbe > 7:  
    print('Invalid')  
for day in days:  
    if day == numbe:  
        print(days[day])  


# PROBLEM 11  
# Discount Based on Bill  
bill = int(input('Enter your bill: '))  
if bill >= 1000:  
    twen_per = 20 / 100 * bill  
    final = bill - twen_per  
    print('You get 20% off')  
elif 500 <= bill <= 999:  
    ten_per = 10 / 100 * bill  
    final = bill - ten_per  
    print('You get 10% off')  
else:  
    final = bill  
    print('You get 0% off')  

print(f'Your final amount is: {final}')
