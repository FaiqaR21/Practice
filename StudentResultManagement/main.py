from models import StudentManager

manager = StudentManager()

while True:

    print("===== Student Result Management =====")

    print("1. Add Student")
    print("2. Add Subject")
    print("3. Record Marks")
    print("4. Display Transcript")
    print("5. Calculate GPA")
    print("6. Top 5 Students")
    print("7. Export CSV")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.add_subject()

    elif choice == "3":
        manager.record_marks()

    elif choice == "4":
        manager.display_transcript()

    elif choice == "5":
        manager.calculate_gpa()

    elif choice == "6":
        manager.top_students()

    elif choice == "7":
        manager.export_csv()

    elif choice == "8":
        manager.close()
        print("Program Closed")
        break

    else:
        print("Invalid Choice")