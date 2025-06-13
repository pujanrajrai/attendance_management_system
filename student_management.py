def add_student_record():
    roll_no = input("Enter Your Roll No")
    name = input("Enter Your Name")
    contact_no = input("Enter Your Contact No")

    with open("student.txt", "r") as student_record:
        students = student_record.readlines()
        for student in students:
            student = student.strip()
            if student.startswith(f"{roll_no}"+","):
                print("Student With This Roll No already Exist")
                return

    with open("student.txt", "a") as file:
        file.write(f"{roll_no},{name},{contact_no}\n")
    print("Student Record Added Successfully")


def view_student_record():
    with open("student.txt", "r") as student_data:
        students = student_data.readlines()
        for student in students:
            print(student.strip())


def update_student_record():
    roll_no = input("Enter Student Roll No:")
    is_update = False
    updated_record = []
    # step 1 read student record
    with open("student.txt", "r") as file:
        students = file.readlines()
        for student in students:
            student_record = student.strip().split(",")
            student_roll = student_record[0]
            if student_roll == roll_no:
                print(f"Student Records: {student_record}")
                name = input("Enter Your Name: ")
                contact_no = input("Enter Your Contact No: ")
                updated_record.append(f"{roll_no}, {name}, {contact_no}\n")
                is_update = True
            else:
                updated_record.append(student)
        if is_update:
            with open("student.txt", "w") as file:
                file.writelines(updated_record)
            print("Student record updated successfully.")
        else:
            print("Student record not found.")


def delete_student():
    roll_no = input("Enter Student Roll No:")
    is_deleted = False
    updated_record = []
    # step 1 read student record
    with open("student.txt", "r") as file:
        students = file.readlines()
        for student in students:
            student_record = student.strip().split(",")
            student_roll = student_record[0]
            if student_roll == roll_no:
                print(f"Student Records: {student_record}")
                is_deleted = True
            else:
                updated_record.append(student)
        if is_deleted:
            with open("student.txt", "w") as file:
                file.writelines(updated_record)
            print("Student record Deleted successfully.")
        else:
            print("Student record not found.")
