# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 21,
    "city": "Chennai",
    "course": "Python"
}

# Printing the dictionary
print("Dictionary:", my_dict)

# Accessing elements using keys
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])
print("Course:", my_dict["course"])

# Accessing using get()
print("Name:", my_dict.get("name"))

# Accessing all keys
print("Keys:", my_dict.keys())

# Accessing all values
print("Values:", my_dict.values())

# Accessing all key-value pairs
print("Items:", my_dict.items())

# Accessing using for loop
print("All elements:")
for key, value in my_dict.items():
    print(key, ":", value)

# Finding dictionary length
print("Length:", len(my_dict))