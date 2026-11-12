
s = set()
print(s)

# Set with numbers
s = {10, 20, 30, 40}
print(s)

# Set with strings
s = {"apple", "banana", "mango"}
print(s)

# Duplicate values
s = {10, 20, 10, 30, 20}
print(s)  # {10, 20, 30}
s = {10, 20, 30}
s.add(40)
print(s)