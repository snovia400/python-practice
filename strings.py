#  Easy (1–5)
# Basic Greeting
# Take your name as input and print: "Hello, [name]!"

# String Length
# Write a function that takes a string and prints its length.

# Uppercase Converter
# Convert a given string to uppercase.

# Count Spaces
# Count how many spaces are in a sentence.

# First and Last Character
# Print the first and last character of a string.



name  = input('enter your name: ')
print(f'hello {name}!')

s = input('enter a string: ')
print(f'the length is {len(s)} ')

st = input('enter string: ')
upper = st.upper()
print(upper)

sen = input('enter a sentence: ')
count = sen.count(' ')
print(count)

w = input('enter a word: ')
first = w[0]
last = w[-1]
print(f'first letter is {first} and last is {last}')






# Medium (6–10)
# Vowel Counter
# Count the number of vowels in a string.

# Reverse a String
# Return the reverse of a given string.

# Check Palindrome
# Write a function that checks if a string is a palindrome.

# Replace Word
# Replace all "bad" in a sentence with "good".

# Word Splitter
# Split a sentence into words and print the list



stri = input('enter a string: ')
count = 0
for i in stri:
    if i.lower() in 'aeiou':
           count += 1
print(count)


worr = input('enter a string: ')
rev = worr[::-1]
print(rev)


wo = input('enter a string: ')
rever = wo[::-1]
if rever == wo:
    print('palindromic')
else:     
    print('not palindromic')




a = input('enter a sentence')
rep = a.replace('bad','good')
print(rep)


snet =  input('enter a sentence: ')
li = snet.split(' ')
print(li)



# Challenging / Fun (11–15)
# Remove Punctuation
# Remove all punctuation from a string (hint: use string.punctuation).

# Most Frequent Character
# Find the character that appears the most in a string.

# Find Substring
# Check if one string is a part of another.

# Alternate Case
# Convert every alternate character in a string to uppercase (hElLo style).

# Custom Join
# Given a list of words, join them using "🎉" between each.


import string
inp = input('enter strings with punc: ')

for char in string.punctuation:
   inp = inp.replace(char,'')
print(inp)


fre = input('enter a string: ')
dictio = {}

for i in fre:
   countt =  fre.count(i)
   dictio[i] = countt

val = 0
freq = ''
for i in dictio:
   if i == ' ':
      continue
   if dictio.get(i)>val:
      freq = i
      val = dictio[i]
print(freq)



senten = input('enter a sentence: ')
word = input('enter the word u want to find: ')
if word.lower() in senten:
    print('found!')
else:
    print('not found')


hell = input('enter a string to style it: ')
for i in range(len(hell)):
    if i % 2 == 0:
        print(hell[i].lower(),end='')
    else:
        print(hell[i].upper(),end='')


wordss = input('enter the sentence to seperate: ')
lis = wordss.split(' ')
lol = '🎉'.join(lis)
print(lol)