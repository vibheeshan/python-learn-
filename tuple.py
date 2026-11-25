
# Python Tuple Practice

# 1. Creating a tuple
t = (10, 20, 30, 40, 50)
print("Tuple:", t)

# 2. Accessing elements
print("First element:", t[0])
print("Last element:", t[-1])

# 3. Finding length
print("Length:", len(t))

# 4. Slicing
print("Slicing:", t[1:4])

# 5. Counting elements
print("Count:", t.count(10))

# 6. Finding index
print("Index:", t.index(30))

# 7. Checking element
print("Is 30 present?", 30 in t)

# 8. Maximum and minimum
print("Maximum:", max(t))
print("Minimum:", min(t))

# 9. Sum of elements
print("Sum:", sum(t))

# 10. Average
print("Average:", sum(t) / len(t))

# 11. Reversing tuple
print("Reverse:", t[::-1])

# 12. Concatenating tuples
t1 = (10, 20, 30)
t2 = (40, 50, 60)
print("Concatenation:", t1 + t2)

# 13. Repeating tuple
print("Repeat:", t1 * 2)

# 14. Converting list into tuple
my_list = [1, 2, 3, 4]
new_tuple = tuple(my_list)
print("List to Tuple:", new_tuple)

# 15. Converting tuple into list
my_tuple = (1, 2, 3, 4)
new_list = list(my_tuple)
print("Tuple to List:", new_list)

# 16. Converting string into tuple
s = "Python"
print("String to Tuple:", tuple(s))

# 17. Printing elements using loop
print("Tuple elements:")
for i in t:
    print(i)

# 18. Printing elements using index
for i in range(len(t)):
    print("Index:", i, "Value:", t[i])

# 19. Printing even numbers
print("Even numbers:")
for i in t:
    if i % 2 == 0:
        print(i)

# 20. Printing odd numbers
print("Odd numbers:")
for i in t:
    if i % 2 != 0:
        print(i)

# 21. Counting even and odd numbers
even = 0
odd = 0

for i in t:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)

# 22. Finding second largest number
numbers = (10, 50, 30, 20, 40)
unique = sorted(set(numbers))
print("Second largest:", unique[-2])

# 23. Finding common elements
a = (10, 20, 30, 40)
b = (30, 40, 50, 60)

common = tuple(i for i in a if i in b)
print("Common elements:", common)

# 24. Removing duplicates
values = (10, 20, 10, 30, 20, 40)
unique_values = tuple(dict.fromkeys(values))
print("Without duplicates:", unique_values)

# 25. Checking tuple equality
x = (1, 2, 3)
y = (1, 2, 3)
print("Are tuples equal?", x == y)
