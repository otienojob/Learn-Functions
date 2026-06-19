studentProfile={}

while True:
    print("---Menu Options---")
    print(f"1. Add Student Details: \n")
    print(f"2. View Student Profile: \n")
    print(f"3. Update Student Details: \n")
    print(f"4. Delete Student Details: \n")
    print(f"5. Exit: \n)")
#Select user input
    
    menu_pick=input(f"Select a menu item: ").strip()
    if menu_pick == "1":
        student_name=input(f"Enter Student's Name - First & Second Name \n").strip().upper()
        #if student_name:
        #    break
        #print("Name cannot be empty")

        while True:
            student_age=int(input(f"Enter Student's Age: \n").strip())
            if student_age:
                break
            print(f"Value cannot be empty or null!")

        while True:
            studentGender=input(f"Enter the Student's gender: \n").strip().upper()
            if studentGender in ["M","F","Male","Female"]:
                break
            print(f"Enter a valide gender entry - M or F or Male or Female ")
        #store dictionary details
                
        studentProfile={
            "Student Names":student_name,
            "Student Age":student_age,
            "Student Gender":studentGender
            }
        print(f"You have successfully created the student's profile")
        print(studentProfile)

    elif menu_pick=="2":
        print(studentProfile)
