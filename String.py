
text = input("Enter a string: ")

print("\n--- STRING OPERATIONS ---")

# 1. Original String
print("Original String:", text)

# 2. Length
print("Length:", len(text))

# 3. Uppercase
print("Uppercase:", text.upper())

# 4. Lowercase
print("Lowercase:", text.lower())

# 5. Capitalize
print("Capitalize:", text.capitalize())

# 6. Title
print("Title:", text.title())

# 7. Reverse
print("Reverse:", text[::-1])

# 8. First Character
print("First Character:", text[0])

# 9. Last Character
print("Last Character:", text[-1])

# 10. Slicing
print("First 3 Characters:", text[:3])

# 11. Replace
print("Replace:", text.replace("a", "b"))

# 12. Count
print("Count of a:", text.count("a"))

# 13. Find
print("Find a:", text.find("a"))

# 14. Remove Spaces
print("Remove Spaces:", text.strip())

# 15. Split
print("Split:", text.split())

# 16. Check Alphabet
print("Is Alphabet:", text.isalpha())

# 17. Check Digit
print("Is Digit:", text.isdigit())

# 18. Check Alphanumeric
print("Is Alphanumeric:", text.isalnum())

# 19. Check Uppercase
print("Is Uppercase:", text.isupper())

# 20. Check Lowercase
print("Is Lowercase:", text.islower())

# 21. Starts With
print("Starts with H:", text.startswith("H"))

# 22. Ends With
print("Ends with n:", text.endswith("n"))

# 23. Concatenation
print("Concatenation:", text + " Python")

# 24. Repetition
print("Repetition:", text * 2)
