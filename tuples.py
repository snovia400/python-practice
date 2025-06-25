#  Easy (1–4)
# 1. Create a tuple of 5 favorite colors and print it.
# 2. Print the 1st and last item in a tuple.
# 3. Check if "blue" is in the tuple colors.
# 4. Try changing an element of a tuple. What happens?

clrs = ('blue','pink','black','white','purple')
print(clrs)


a = (1,2,3,4,5)
f = a[0]
l = a[-1]

print(f'first item is {f} and last item is {l}')


print('blue' in  clrs)


# a[0] = 90
# print(a) #throws an error


# Medium (5–7)
# 5. Count how many times 3 appears in this tuple:

# nums = (1, 2, 3, 4, 3, 3, 5)
# 6. Find the index of "banana" in this tuple:

# fruits = ("apple", "banana", "cherry")
# 7. Convert this list to a tuple:

# lst = [10, 20, 30]


nums = (1, 2, 3, 4, 3, 3, 5)
print(nums.count(3))


fruits = ("apple", "banana", "cherry")
print(fruits.index('banana'))


lst = [10, 20, 30]
print(tuple(lst))


# Challenging / Fun (8–10)
# 8. Unpack this tuple into 3 variables and print them:

# person = ("Daisy", 13, "Coding")
# 9. Create a tuple inside a list. Print both.
# (Hint: something like [ (a, b), (c, d) ])

# 10. Swap two values using tuple unpacking:

# a = 5  
# b = 10  
# after swap: a = 10, b = 5


person = ('daisy',13,'coding')
name, age , hobby = person
print(name)
print(age)
print(hobby)

b=  [ (1, 2), (3, 4) ]

print(b)


c = 5
d  =10

c ,d = 10 , 5
print(c,d)