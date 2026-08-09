students = []

while True:
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))

        student = {
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)

        print("Student added successfully!")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n===== Student Records =====")

            for student in students:
                print("Name :", student["name"])
                print("Age  :", student["age"])
                print("Marks:", student["marks"])
                print("--------------------")

    # Search Student
    elif choice == "3":
        name = input("Enter student name to search: ")

        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print("\nStudent Found!")
                print("Name :", student["name"])
                print("Age  :", student["age"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    # Update Marks
    elif choice == "4":
        name = input("Enter student name: ")

        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                new_marks = float(input("Enter new marks: "))
                student["marks"] = new_marks

                print("Marks updated successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == "5":
        name = input("Enter student name to delete: ")

        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                students.remove(student)

                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "6":
        print("Thank you for using Student Record Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
