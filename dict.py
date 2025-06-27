# Easy (1–7): Basics & Access
# Create a dictionary with keys "name", "age", "hobby" and print it.

# Access and print the value for "age".

# Add a new key "city" with a value.

# Change the value of "hobby" to something new.

# Remove the "age" key from the dictionary.

# Check if "name" exists in the dictionary.

# Loop through the dictionary and print each key and value.


dic1  = {
    'name' : 'snovia',
    'age' : 12,
    'hobby' : 'coding'
}
print(dic1)


print(dic1['age'])

dic1.update({'city' : 'karachi'})
print(dic1)

dic1.update({'hobby':'drawing'})
print(dic1)

del dic1['age']
print(dic1)

print('name' in dic1)

for k , v  in dic1.items():
    print(k , v)




# Medium (8–16): Logic & Operations
# Count the frequency of each letter in a word.

# Merge two dictionaries.

# Get all keys from a dictionary.

# Get all values from a dictionary.

# Create a dictionary from two lists using zip().

# Sort a dictionary by keys.

# Sort a dictionary by values.

# Create a dictionary with numbers from 1 to 5 and their squares.

# Swap keys and values in a dictionary (values must be unique).


a = {}
w = input('enter a word: ')
for i in w:
   cnt = w.count(i)
   a.update({i : cnt})
print(a)

freq = ''
max = 0
for i in a:
   if a[i] > max:
      max = a[i]
      freq = i
print(freq)


dic1.update(a)
print(dic1)

print(a.keys())
print(a.values())



l1 = ['x','b','w','d']
l2 = [1,7,3,4]

o = dict(zip(l1,l2))
print(o)


sort = sorted(o.keys())
print(sort)


sort = sorted(o.values())
print(sort)


sqs = {}

for i in range(1,6):
      sqs[i] = i **2
   

print(sqs)


new  = {}
for key,value in sqs.items():
   new[value] = key
print(new)




# Challenging (17–23): Nested & Advanced
# Create a nested dictionary for a student with "name", "grades", "address".

# Access a nested value from that dictionary.

# Create a dictionary that stores the number of vowels in a sentence.

# Count how many times each word appears in a sentence.

# Group words by their length.

# Find the key with the maximum value in a dictionary.

# Write a program that lets the user enter names and scores, and stores them in a dictionary.


stud = {
    'name' : 'snovia',
    'address' : 'xyz',
    'grades' : {
        'math' : 97,
        'comp' : 100,
        'science' : 96
    }


}

print(stud['grades']['math'])

sent = input('enter a sentence: ')

vowels = {}
cnt = 0

for i in sent:
    if i.lower() in 'aeiou':
        cnt = sent.count(i)
        vowels[i] = cnt
print(vowels)


stringg = input('enter a string: ')
l = stringg.split(' ')
words  = {}
cnt = 0
for i in l:
   cnt =  l.count(i)
   words[i] = cnt
print(words)


string = input('enter a string: ')
l  = string.split()
ln  = 0
wrds = {}

for i in l:
   ln = len(i)
   if ln in wrds:
      wrds[ln].append(i)
   else:
      wrds[ln] = [i]
print(wrds)



grades = {
        'math' : 97,
        'comp' : 100,
        'science' : 99}

max = 0
maxs = ''
for key , val in grades.items():
    if val > max:
        max = val
        maxs = key
print(f'the highest marks are {max} in {maxs}')



dic = {

}

for i in range(1,4):
  name = input('enter name: ')
  score = input('enter score: ')
  dic[name] = score
print(dic) 