from operations import StudentManagementSystem
from student import Student

def get_valid_input(prompt, cast_type, condition=None):
    """Helper function to validate user input and prevent crashes."""
    while True:
        try:
            value = cast_type(input(prompt))
            if condition and not condition(value):
                print("Invalid input! Please meet the required constraints.")
                continue
            return value
        except ValueError:
            print(f"Invalid type! Expected a/an {cast_type.__name__}.")

def main():
    sms = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Generate Reports")
        print("7. Export to CSV")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            s_id = get_valid_input("Student ID (integer): ", int)
            name = input("Name: ")
            age = get_valid_input("Age: ", int, lambda x: x > 0)
            grade = get_valid_input("Grade (0-100): ", float, lambda x: 0 <= x <= 100)
            att = get_valid_input("Attendance (0-100): ", float, lambda x: 0 <= x <= 100)
            email = input("Email (optional): ")
            
            student = Student(s_id, name, age, grade, att, email)
            if sms.add_student(student):
                print("Student added successfully!")

        elif choice == '2':
            sort_choice = input("Sort by (1) None, (2) Grade, (3) Attendance: ")
            sort_by = None
            if sort_choice == '2': sort_by = 'grade'
            elif sort_choice == '3': sort_by = 'attendance'

            students = sms.get_all_students(sort_by)
            if not students:
                print("No students found.")
            for s in students:
                print(f"[{s.student_id}] {s.name} - Age: {s.age}, Grade: {s.grade}, Att: {s.attendance}%, Email: {s.email}")

        elif choice == '3':
            s_id = get_valid_input("Enter ID of student to update: ", int)
            name = input("New Name: ")
            age = get_valid_input("New Age: ", int, lambda x: x > 0)
            grade = get_valid_input("New Grade (0-100): ", float, lambda x: 0 <= x <= 100)
            att = get_valid_input("New Attendance (0-100): ", float, lambda x: 0 <= x <= 100)
            email = input("New Email (optional): ")
            
            sms.update_student(s_id, name, age, grade, att, email)
            print("Student updated successfully!")

        elif choice == '4':
            s_id = get_valid_input("Enter ID of student to delete: ", int)
            sms.delete_student(s_id)
            print("Student deleted!")

        elif choice == '5':
            term = input("Enter Name or ID to search: ")
            results = sms.search_student(term)
            if not results:
                print("No matches found.")
            for s in results:
                print(f"Match found: [{s.student_id}] {s.name} (Grade: {s.grade})")

        elif choice == '6':
            print("\n--- System Reports ---")
            print(f"Total Students: {sms.get_total_students()}")
            print(f"Average Grade: {sms.get_average_grade():.2f}")
            
            top = sms.get_highest_attendance()
            if top:
                print(f"Highest Attendance: {top.name} ({top.attendance}%)")
                
            fails = sms.get_failing_students()
            print("Failing Students (Grade < 50):")
            if not fails:
                print(" - None! All students are passing.")
            for f in fails:
                print(f" - [{f.student_id}] {f.name} (Grade: {f.grade})")

        elif choice == '7':
            sms.export_to_csv()
            print("Data exported to 'students.csv' successfully.")

        elif choice == '8':
            print("Exiting Student Management System. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()