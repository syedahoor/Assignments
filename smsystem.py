students = {}

while True:
    print("\n***** Student Management System *****")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Find Average Marks")
    print("8. Count Students")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student Added")

    elif choice == 2:
        if students:
            for name, marks in students.items():
                print(name, ":", marks)
        else:
            print("No Students Found")

    elif choice == 3:
        name = input("Enter student name: ")
        if name in students:
            print("Marks =", students[name])
        else:
            print("Student Not Found")

    elif choice == 4:
        name = input("Enter student name: ")
        if name in students:
            students[name] = int(input("Enter new marks: "))
            print("Marks Updated")
        else:
            print("Student Not Found")

    elif choice == 5:
        name = input("Enter student name: ")
        if name in students:
            del students[name]
            print("Student Deleted")
        else:
            print("Student Not Found")

    elif choice == 6:
        if students:
            topper = max(students, key=students.get)
            print("Topper:", topper)
            print("Marks:", students[topper])
        else:
            print("No Students Found")

    elif choice == 7:
        if students:
            avg = sum(students.values()) / len(students)
            print("Average Marks =", avg)
        else:
            print("No Students Found")

    elif choice == 8:
        print("Total Students =", len(students))

    elif choice == 9:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
