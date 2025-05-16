def add_student_record():
    print("you are on student add record")


def view_student_record():
    print("you are on student view record")


def update_student_record():
    print("you are on student update record")


def menu():
    run = True
    while run:
        print("Etner 1 To Add Student")
        print("Enter 2 To View Student Details")
        print("Etner 3 to Update Student")
        print("Etner 4 To Delete Student")
        print("Etner 5 To Take Attendance")
        print("Enter 6 to View Attendance")
        print("Enter 8 to end")
        option = input()
        if option == "1":
            add_student_record()
        elif option == "2":
            view_student_record()
        elif option == "3":
            update_student_record()
        elif option == "8":
            run = False
        else:
            print("Invalid choices")


menu()
