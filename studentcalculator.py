
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

m1 = int(input("Enter Tamil mark: "))
m2 = int(input("Enter English mark: "))
m3 = int(input("Enter Maths mark: "))
m4 = int(input("Enter Science mark: "))
m5 = int(input("Enter Social mark: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("\n----- STUDENT RESULT -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")
