principal = float(input("Principal amount: "))
rate = float(input("Rate of interest (%): "))
time = float(input("Time (years): "))
interest = (principal * rate * time) / 100
print("Simple interest:", interest)
print("Total amount:", principal + interest)