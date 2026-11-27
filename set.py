
# 1. Create an empty set
s = set()
print("Empty set:", s)

# 2. Set with numbers
s = {10, 20, 30, 40}
print("Numbers:", s)

# 3. Set with strings
s = {"apple", "banana", "mango"}
print("Strings:", s)

# 4. Duplicate values (automatically removed)
s = {10, 20, 10, 30, 20}
print("Duplicates removed:", s)

# 5. Add an element
s = {10, 20, 30}
s.add(40)
print("Add:", s)

# 6. Add multiple elements
s.update([50, 60, 70])
print("Update:", s)

# 7. Remove an element (raises error if absent)
s.remove(20)
print("Remove:", s)

# 8. Discard an element (no error if absent)
s.discard(100)
print("Discard:", s)

# 9. Pop an element (removes an arbitrary element)
s.pop()
print("Pop:", s)

# 10. Check element exists
s = {10, 20, 30}
print("Exists:", 20 in s)
print("Not exists:", 50 not in s)


# 21. Difference update
a = {1, 2, 3}
b = {2, 3, 4}
a.difference_update(b)
print("Difference Update:", a)

# 22. Intersection update
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print("Intersection Update:", a)

# 23. Symmetric difference update
a = {1, 2, 3}
b = {2, 3, 4}
a.symmetric_difference_update(b)
print("Symmetric Difference Update:", a)

# 24. Update using another set
a = {1, 2}
a.update({3, 4})
print("Set Update:", a)

# 25. Frozenset (immutable set)
fs = frozenset([10, 20, 30])
print("Frozenset:", fs)
