studentProfile={}

while True:
    print("---Menu Options---")
    print(f"1. Add Student Details: \n")
    print(f"2. View Student Profile: \n")
    print(f"3. Exit: ")
#Select user input
    
    menu_pick=input(f"Select a menu item: ").strip()

    if menu_pick == "1":
        while True:
            student_name=input(f"Enter Student's Name - First & Second Name \n").strip().title()
            
            if student_name:
                break
            print("Student Name cannot be empty")

        while True:
            try:
                student_age=int(input(f"Enter Student's Age: \n").strip())
                if student_age > 0:
                    break
                print(f"Value cannot be less than zero!")
            except ValueError:
                print(f"Value must be an integer")

        while True:
            studentGender=input(f"Enter the Student's gender - M/F: \n").strip().upper()
            if studentGender in ["M","F","MALE","FEMALE"]:
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
        if studentProfile:
            print("\n--- STUDENT PROFILE ---")

            for key, value in studentProfile.items():

                print(f"{key}: {value}")

        else:

            print("No student profile found.")

    elif menu_pick == "3":

        print(f"Goodbye!")

        break

    else:

        print("Invalid menu option. Try again.")
