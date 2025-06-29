# 📁 Easy (1–3): File Basics
# Write to a File
# Write "Hello, world!" into a file named hello.txt.

# Read a File
# Read and print the contents of hello.txt.

# Append to a File
# Add "Goodbye, world!" to the end of hello.txt.


with open ('hello.txt', 'w') as hi:
    hi.write('Hello!,World')
 
    


with open('hello.txt','r') as a:
    print(a.read())



with open ('hello.txt','a') as b:
    b.write(' \ngoodbye world')







# 📝 Medium (4–6): Line-by-Line Handling
# Count Lines in a File
# Count how many lines are in hello.txt.

# Read First Line Only
# Read and print only the first line of hello.txt.

# Write a List to File
# Given a list of fruits, write each fruit on a new line in a file fruits.txt.
# fruits = ['apple', 'banana', 'cherry']

with open ('hello.txt' , 'r') as c:
    cnt = 0
    for i in c.readlines():
        cnt+=1
    print(cnt)

with open ('hello.txt' , 'r') as o:
    o.readline()

fruits = ['apple', 'banana', 'cherry']
with open('fruits.txt' , 'w') as x:
    for i in fruits:
        x.write(f'{i}\n')


# 🧠 Challenging (7–9): Logic + Files
# Count Words in a File
# Count and print the number of words in fruits.txt.

# Search for a Word in File
# Ask the user for a word and check if it exists in fruits.txt.

# Copy Contents
# Copy the contents of fruits.txt to a new file called backup.txt.

with open ('fruits.txt','r') as f:
  with open('fruits.txt', 'r') as f:
    text = f.read()
    words = text.split()  
    print(len(words))     


w = input('enter the word: ')

with open('fruits.txt', 'r') as f:
        cont = f.read()
        if w in cont:
           print('found!!')
        else:
           print('not found!')


with open('fruits.txt', 'r') as g:
    content = g.read()
    with open('backup.txt', 'w') as p:
        p.write(content)
