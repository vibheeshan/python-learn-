# Read scores until 0, then print the count and the total
count = 0
total = 0
score = int(input())
while score != 0:
    count += 1
    total += score
    score = int(input())
print(f"Count: {count}")
print(f"Total: {total}")
