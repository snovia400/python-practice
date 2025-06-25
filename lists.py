# Easy (1–6)
# Basic List Handling

# Create a list of 5 fruits and print it.

# Access and print the 1st and last item of a list.

# Add an element to a list and print the updated list.

# Remove an element from a list.

# Find the length of a list.

# Check if "apple" is in the list

fr = ['apple','orange','cherry','grapes','strawberry']
print(fr)

a = ['ff',2,'okoko',4,True]
print(a[0],a[-1])

b = [1,2,3,4,5]
b.append(6)
print(b)

c = ['hi','hello','ko']
print(len(c))

print( 'apple'.lower() in fr )


# Medium (7–12)
# Looping, Filtering, Summing
# 7. Print each item in a list using a loop.
# 8. Find the sum of all numbers in a list.
# 9. Count how many even numbers are in a list.
# 10. Create a new list with only odd numbers from a given list.
# 11. Sort a list of numbers and print it.
# 12. Reverse a list without using [::-1].

d = [1,2,3,4,5]
for i in d:
    print(i)


e = [1,2,3,4,5]
sum = 0
for i in e:
    sum += i
print(sum)

f = [1,2,3,4,5,6,7,8,9,10]
count = 0
for i in f:
    if i%2 == 0:
        count += 1
print(f'There are {count} even numbers')


g = [4,5,3,3,2,2,21,2,3,5,54,990]
g.sort()
print(g)


h = ['hello','i','am','snovia']
h.reverse()
print(h)



# Challenging (13–18)
# List Comprehensions, Nested Lists
# 13. Use list comprehension to square every number in a list.
# 14. Remove all duplicates from a list.
# 15. Merge two lists into one (without using +).
# 16. Find the second largest number in a list.
# 17. Make a nested list (matrix) and print it row by row.
# 18. From a list of words, create a new list with only words longer than 4 letters.

k = [1,2,3,4,5,6]
sq = [i**2 for i in k]
print(sq)

l = [1,1,2,2,3,3,4,4,5,5,1,2]
unique = []
for i in l:
   if i not in unique:
       unique.append(i)
print(unique)


l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l1.extend(l2)
print(l1)


r = [1,5,3,7,8,5678,45678765,7774,2345676543]
lar = 0
sec = 0
for i in r:
    if i > lar:
        lar = i
    
for i in r:
    if i > sec and i < lar:
        sec = i        
print(sec)


matrix = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]

for row in matrix:
    print(row)

o = ['hello','koooo','hhhhhhhh','jo','ekii','hhhhhh','ppp']
new = []
for i in o:
    if len(i) > 4:
        new.append(i)

print(new)