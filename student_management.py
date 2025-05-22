def add_student_record():
    roll_no = input("Enter Your Roll No")
    name = input("Enter Your Name")
    contact_no = input("Enter Your Contact No")
    with open("student.txt", "a") as file:
        file.write(f"{roll_no},{name},{contact_no}\n")
    print("Student Record Added Successfully")


def view_student_record():
    print("you are on student view record")


def update_student_record():
    print("you are on student update record")


def delete_student():
    print("You are on Delete Student")
