Exam={}

while True:
    print("---Menu Options---")
    print(f"1. Add Student Details: \n")
    print(f"2. Update Student Details: \n")
    print(f"3. Delete Student Details: \n")
    print(f"4. Exit: \n)")

    menu_pick=input(f"Select action item: ").strip()
    if menu_pick == "1":
        student_name=input(f"Enter Student's Name - First & Second Name \n").strip()
        if student_name:
            break
        print("Name cannot be empty")

        while True:
            student_age=int(input(f"Enter Student's Age: \n").strip())
            break
        print(f"The age has to be an integer!")
        while True:
            studentGender=input(f"Enter the Student's gender: \n").strip().upper()
            if studentGender in ["M","F","Male","Female"]
            break
        print(f"Enter a valide gender entry - M or F or Male or Female ")