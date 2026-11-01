n = input()
s = str(n)
l = len(s)

if n[0] == n[l-1]:
    print("Match")
else:
    print("Not Match")