#  Easy (1–5): Understand the Basics
# Create a list of dictionaries with 3 students (name & age), and print it.

# Access the age of the second student in the list.

# Create a dictionary where each key is a subject and the value is a list of marks.

# Print the 2nd mark in "math" from the dictionary.

# Loop through the list of students and print each name.





std = [
    {'name': 'ali', 'age' : 17},
    {'name': 'anna', 'age' : 9},
    {'name': 'any', 'age' : 10}
]

print(std[1] ['age'])


marks = {
    'math': [90,89,98],
    'science': [100,79,94]
}
print(marks['math'][1])


for i in std:
    print(i['name'])


# Medium (6–11): Access & Manipulate
# Add a new subject and marks list to the subject-marks dictionary.

# Change the third student's age to 15.

# Add a new mark to the "science" subject.

# From a list of dictionaries, print only the students above age 12.

# count how many students are age 10 or above..

# From a dictionary of subjects with mark lists, find the subject with the highest average.


marks['english'] = [68 , 99 , 78]

print(marks)



for i in std:
    if i == std[2]:
        i.update({'age': 15})
print(std)


marks['science'].append(66)    
print(marks)


for i in std:
    if i['age'] > 12:
        print(i)

count = 0
for i in std:
    if i['age'] >= 10:
        count += 1
print(count)

marks = {
    'math': [90,89,98],
    'science': [100,79,94],
    'geography': [101,99,97],
    'english': [60,59,84]
}



def avg(d):
    biggest = 0
    l = []
    t = 0
    for i in d.values():
        t = 0
        for j in i:
          t += j
        avg = t / len(i)
        l.append(avg)
    for big in l:
       if big > biggest:
          biggest = big
    
    print(biggest)
avg(marks)


# Challenging (12–16): Logic Practice
# Create a nested dictionary for 2 employees with keys: name, salary, skills (list).

# Print the second skill of employee 1.

# Count how many students scored above 90 in "math" from a class record (nested dict).

# Create a dictionary where each key is a student's name and value is another dictionary with subjects and scores.

# From that nested dictionary, print the name of the student with the highest score in "science"


employees = {
    'emp1' : {
        'name' : 'snovia',
        'salary' : 10000000000,
        'skills' : ['skill 1', 'skill 2', 'skill 3']
    },
    'emp2' : {
        'name' : 'anna',
        'salary' : 100,
        'skills' : ['skill 1', 'skill 2', 'skill 3']
    }
    
    
}

print(employees['emp1']['skills'] [1])


students = {
    'Alice': {
        'math': 85,
        'science': 91,
        'english': 78
    },
    'Bob': {
        'math': 92,
        'science': 884,
        'english': 84
    },
    'Charlie': {
        'math': 76,
        'science': 95,
        'english': 80
    }
}

cnt =0
for i in students.values():
      for k,v in i.items():
          if v > 90 and k == 'math':
              cnt+=1

print(cnt)


name = ''
score = 0


for n,s in students.items():
     for k,v in s.items():
        if v > score and k == 'science':
            score = v
            name = n
print(name , score)