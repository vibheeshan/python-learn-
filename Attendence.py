
students = {}
attendance = {}

def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
    else:
        name = input("Enter Student Name: ")
        students[roll] = name
        attendance[roll] = []
        print("Student added successfully!")


def view_students():
    if not students:
        print("No students found!")
    else:
        print("\n--- Student Details ---")
        for roll, name in students.items():
            print("Roll Number:", roll, "| Name:", name)


def mark_attendance():
    roll = input("Enter Roll Number: ")

    if roll in students:
        status = input("Enter P for Present or A for Absent: ")
        status = status.upper()

        if status == "P":
            attendance[roll].append("Present")
            print("Attendance marked as Present!")
        elif status == "A":
            attendance[roll].append("Absent")
            print("Attendance marked as Absent!")
        else:
            print("Invalid attendance status!")
    else:
        print("Student not found!")


def view_attendance():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("\nStudent Name:", students[roll])
        print("Attendance Records:")

        if not attendance[roll]:
            print("No attendance records!")
        else:
            for record in attendance[roll]:
                print(record)
    else:
        print("Student not found!")


def attendance_percentage():
    roll = input("Enter Roll Number: ")

    if roll in students:
        total = len(attendance[roll])

        if total == 0:
            print("No attendance records!")
        else:
            present = attendance[roll].count("Present")
            percentage = (present / total) * 100

            print("Student Name:", students[roll])
            print("Total Classes:", total)
            print("Present:", present)
            print("Absent:", total - present)
            print("Attendance Percentage:", percentage, "%")
    else:
        print("Student not found!")


while True:
    print("\n===== STUDENT ATTENDANCE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Attendance Percentage")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        mark_attendance()
    elif choice == "4":
        view_attendance()
    elif choice == "5":
        attendance_percentage()
    elif choice == "6":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice! Please try again.")
