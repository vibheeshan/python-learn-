# Learn Basic Python (Short & Simple)

Each example is only a few lines. Copy it, run it, change it.

Run any file with: `python file.py`

---

## 1. Print

```python
print("Hello, world!")
```

## 2. Variables

```python
name = "Asha"
age = 20
print(name, age)
```

## 3. Math

```python
print(5 + 3)   # 8
print(10 / 4)  # 2.5
print(10 // 4) # 2
print(2 ** 3)  # 8
```

## 4. Input

```python
name = input("Your name? ")
print("Hi", name)
```

## 5. If / Else

```python
n = 7
if n % 2 == 0:
    print("even")
else:
    print("odd")
```

## 6. Loops

```python
for i in range(5):
    print(i)

count = 0
while count < 3:
    print("count", count)
    count += 1
```

## 7. Lists

```python
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits[0], len(fruits))
for f in fruits:
    print(f)
```

## 8. Dictionaries

```python
person = {"name": "Asha", "age": 20}
print(person["name"])
person["city"] = "Chennai"
```

## 9. Functions

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

## 10. Strings

```python
s = "hello"
print(s.upper(), s[0], len(s))
print(f"Say {s} to me")
```

## 11. Read / Write a File

```python
with open("note.txt", "w") as f:
    f.write("hi")

with open("note.txt") as f:
    print(f.read())
```

## 12. Try / Except

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("can't divide by zero")
```

---

## Mini Practice

1. Print the numbers 1 to 10.
2. Ask for a number and say if it is even or odd.
3. Make a list of 3 foods and print each one.
4. Write a function that returns the square of a number.

Keep going: try small programs, break things, and read the error messages.