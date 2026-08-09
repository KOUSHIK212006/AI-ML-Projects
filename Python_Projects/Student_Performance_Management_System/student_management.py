import re

students = []

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Enter Marks")
    print("5. Calculate Result")
    print("6. Class Statistics")
    print("7. Student Ranking")
    print("8. Remove Student")
    print("9. Exit")

    n = int(input("Enter your choice: "))

    # --------------------------------------------------
    # PART 1 - ADD STUDENT
    # --------------------------------------------------

    if n == 1:

        name = input("Enter the name of student: ").strip()
        usn = input("Enter the USN of student: ").strip().upper()

        # Email validation using Regex
        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        while True:

            email = input("Enter Email: ").strip()

            if re.fullmatch(email_pattern, email):
                break

            print("Invalid email. Please enter a valid email.")

        age = int(input("Enter age: "))

        student = {
            "name": name,
            "usn": usn,
            "email": email,
            "age": age,
            "marks": {}
        }

        students.append(student)

        print("Student added successfully!")

    # --------------------------------------------------
    # PART 2 - VIEW STUDENTS
    # --------------------------------------------------

    elif n == 2:

        if not students:

            print("No student entered yet.")

        else:

            print("\n===== STUDENTS =====")

            for student in students:

                print(f"""
Name  : {student["name"]}
USN   : {student["usn"]}
Email : {student["email"]}
Age   : {student["age"]}
---------------------
""")

    # --------------------------------------------------
    # PART 3 - SEARCH STUDENT
    # --------------------------------------------------

    elif n == 3:

        detail = input(
            "Enter Student Name or USN to search: "
        ).strip().upper()

        found = False

        for student in students:

            if (
                detail == student["name"].upper()
                or
                detail == student["usn"].upper()
            ):

                print("\n===== STUDENT FOUND =====")

                print("Name  :", student["name"])
                print("USN   :", student["usn"])
                print("Email :", student["email"])
                print("Age   :", student["age"])

                found = True
                break

        if not found:

            print("Student not found.")

    # --------------------------------------------------
    # PART 4 - ENTER MARKS
    # --------------------------------------------------

    elif n == 4:

        usn = input("Enter USN: ").strip().upper()

        found = False

        for student in students:

            if student["usn"].upper() == usn:

                found = True

                # Python
                pythonMark = int(
                    input("Enter Python marks: ")
                )

                while pythonMark < 0 or pythonMark > 100:

                    print("Marks must be between 0 and 100")

                    pythonMark = int(
                        input("Enter Python marks: ")
                    )

                student["marks"]["Python"] = pythonMark

                # DSA
                dsaMark = int(
                    input("Enter DSA marks: ")
                )

                while dsaMark < 0 or dsaMark > 100:

                    print("Marks must be between 0 and 100")

                    dsaMark = int(
                        input("Enter DSA marks: ")
                    )

                student["marks"]["DSA"] = dsaMark

                # Mathematics
                mathMark = int(
                    input("Enter Mathematics marks: ")
                )

                while mathMark < 0 or mathMark > 100:

                    print("Marks must be between 0 and 100")

                    mathMark = int(
                        input("Enter Mathematics marks: ")
                    )

                student["marks"]["Mathematics"] = mathMark

                # AI
                aiMark = int(
                    input("Enter AI marks: ")
                )

                while aiMark < 0 or aiMark > 100:

                    print("Marks must be between 0 and 100")

                    aiMark = int(
                        input("Enter AI marks: ")
                    )

                student["marks"]["AI"] = aiMark

                # Computer Science
                csMark = int(
                    input("Enter Computer Science marks: ")
                )

                while csMark < 0 or csMark > 100:

                    print("Marks must be between 0 and 100")

                    csMark = int(
                        input("Enter Computer Science marks: ")
                    )

                student["marks"]["Computer Science"] = csMark

                print("Marks saved successfully!")

                break

        if not found:

            print("Student not found.")

    # --------------------------------------------------
    # PART 5 - CALCULATE RESULT
    # --------------------------------------------------

    elif n == 5:

        usn = input("Enter USN: ").strip().upper()

        found = False

        for student in students:

            if student["usn"].upper() == usn:

                found = True

                if not student["marks"]:

                    print("Marks not entered.")

                else:

                    total = 0
                    passed = True

                    print("\n===== RESULT =====")

                    print("Name :", student["name"])
                    print("USN  :", student["usn"])

                    for subject, marks in student["marks"].items():

                        print(f"{subject}: {marks}")

                        total += marks

                        if marks < 40:

                            print(f"Fail in {subject}")

                            passed = False

                    average = total / len(student["marks"])

                    # Grade calculation
                    if average >= 90:
                        grade = "A+"

                    elif average >= 80:
                        grade = "A"

                    elif average >= 70:
                        grade = "B"

                    elif average >= 60:
                        grade = "C"

                    elif average >= 50:
                        grade = "D"

                    else:
                        grade = "F"

                    print("\nTotal    :", total)
                    print("Average  :", round(average, 2))
                    print("Grade    :", grade)

                    if passed:
                        print("Result   : PASS")

                    else:
                        print("Result   : FAIL")

                break

        if not found:

            print("Student not found.")

    # --------------------------------------------------
    # PART 6 - CLASS STATISTICS
    # --------------------------------------------------

    elif n == 6:

        averages = []

        passed = 0
        failed = 0

        subject_totals = {
            "Python": 0,
            "DSA": 0,
            "Mathematics": 0,
            "AI": 0,
            "Computer Science": 0
        }

        students_with_marks = 0

        for student in students:

            if not student["marks"]:
                continue

            students_with_marks += 1

            total = 0
            student_passed = True

            for subject, marks in student["marks"].items():

                total += marks

                subject_totals[subject] += marks

                if marks < 40:
                    student_passed = False

            average = total / len(student["marks"])

            averages.append(average)

            if student_passed:
                passed += 1
            else:
                failed += 1

        if not averages:

            print("No marks available.")

        else:

            class_average = sum(averages) / len(averages)

            highest_average = max(averages)

            lowest_average = min(averages)

            print("\n===== CLASS STATISTICS =====")

            print(
                "Number of Students :",
                students_with_marks
            )

            print(
                "Class Average      :",
                round(class_average, 2)
            )

            print(
                "Highest Average    :",
                round(highest_average, 2)
            )

            print(
                "Lowest Average     :",
                round(lowest_average, 2)
            )

            print("Passed             :", passed)
            print("Failed             :", failed)

            print("\n===== SUBJECT AVERAGES =====")

            for subject, total in subject_totals.items():

                average = total / students_with_marks

                print(
                    f"{subject:18}: {average:.2f}"
                )

    # --------------------------------------------------
    # PART 7 - STUDENT RANKING
    # --------------------------------------------------

    elif n == 7:

        ranking = []

        for student in students:

            if not student["marks"]:
                continue

            total = 0

            for marks in student["marks"].values():

                total += marks

            average = total / len(student["marks"])

            ranking.append((student, average))

        if not ranking:

            print("No students with marks available.")

        else:

            ranking = sorted(
                ranking,
                key=lambda x: x[1],
                reverse=True
            )

            print("\n===== STUDENT RANKING =====")

            rank = 1

            for student, average in ranking:

                print(
                    f"{rank}. "
                    f"{student['name']} - "
                    f"{average:.2f}"
                )

                rank += 1

    # --------------------------------------------------
    # PART 8 - REMOVE STUDENT
    # --------------------------------------------------

    elif n == 8:

        usn = input("Enter USN: ").strip().upper()

        found = False

        for student in students:

            if student["usn"].upper() == usn:

                students.remove(student)

                print(
                    "Student removed successfully."
                )

                found = True

                break

        if not found:

            print("Student not found.")

    # --------------------------------------------------
    # PART 9 - EXIT
    # --------------------------------------------------

    elif n == 9:

        print(
            "Exiting Student Management System..."
        )

        break

    # --------------------------------------------------
    # INVALID CHOICE
    # --------------------------------------------------

    else:

        print(
            "Invalid choice. "
            "Please enter a number between 1 and 9."
        )
