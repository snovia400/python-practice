# Easy (1–4): Basics of Sets
# Create a set of your 5 favorite foods. Print it.

# Add an item to a set using .add() and print it.

# Remove an item from a set using .remove() and print it.

# Check if "pizza" is in the set.


foods = {'chowmein','rolls','dynamite chicken','shwarma','burgers'}
print(foods)


foods.add('pizza')
print(foods)

foods.remove('rolls')
print(foods)


print('pizza' in foods)



# Medium (5–7): Set Operations
# Find the union of two sets:

# a = {1, 2, 3}  
# b = {3, 4, 5}
# Find the intersection of two sets:
# (same sets above)

# Find the difference (a - b)
# (what’s in a but not in b)


a = {1, 2, 3}  
b = {3, 4, 5}

print(a.union(b))


print(a.intersection(b))

print(a.difference(b))


# Challenging (8–10): Logic & Use Cases
# Given a list with duplicate numbers, convert it to a set to remove duplicates.
# Example:

# nums = [1, 2, 2, 3, 4, 4, 5]
# Use a set to find all unique characters in a string.
# (e.g. "hello" → {'h', 'e', 'l', 'o'})

# Check if two sets are disjoint (have no common elements).
# Use:

# a.isdisjoint(b)

nums =  [1, 2, 2, 3, 4, 4, 5]
nums1 = set(nums)
print(nums1)


string = input('enter a string: ')
uni = set(string)
print(uni)


a = {1,2,3}
b = {4,5,6}
print(a.isdisjoint(b))
