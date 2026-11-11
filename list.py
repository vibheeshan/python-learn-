
# 1. Create a list
a = [10, 20, 30, 40, 50]
print("List:", a)

# 2. Access elements
print("First element:", a[0])
print("Last element:", a[-1])

# 3. Add element
a.append(60)
print("After append:", a)

# 4. Insert element
a.insert(1, 15)
print("After insert:", a)

# 5. Remove element
a.remove(30)
print("After remove:", a)

# 6. Remove last element
a.pop()
print("After pop:", a)

# 7. Find length
print("Length:", len(a))

# 8. Find maximum
print("Maximum:", max(a))

# 9. Find minimum
print("Minimum:", min(a))

# 10. Sort list
a.sort()
print("Sorted:", a)

# 11. Reverse list
a.reverse()
print("Reversed:", a)

# 12. Check element
print("Is 20 present?", 20 in a)

# 13. Print using loop
print("List elements:")
for i in a:
    print(i)

# 14. Sum of elements
print("Sum:", sum(a))

# 15. Clear list
a.clear()
print("After clear:", a)
