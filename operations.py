import csv
from student import Student
import database

class StudentManagementSystem:
    def __init__(self):
        # Ensure database is ready upon system start
        database.initialize_db()

    def add_student(self, student):
        query = "INSERT INTO students (student_id, name, age, grade, attendance, email) VALUES (?, ?, ?, ?, ?, ?)"
        try:
            database.execute_query(query, (student.student_id, student.name, student.age, student.grade, student.attendance, student.email))
            return True
        except Exception as e:
            print(f"Error: Student with ID {student.student_id} may already exist.")
            return False

    def get_all_students(self, sort_by=None):
        query = "SELECT * FROM students"
        
        # Sorting Feature
        if sort_by == 'grade':
            query += " ORDER BY grade DESC"
        elif sort_by == 'attendance':
            query += " ORDER BY attendance DESC"
            
        rows = database.fetch_query(query)
        return [Student(*row) for row in rows]

    def update_student(self, student_id, name, age, grade, attendance, email):
        query = "UPDATE students SET name=?, age=?, grade=?, attendance=?, email=? WHERE student_id=?"
        database.execute_query(query, (name, age, grade, attendance, email, student_id))

    def delete_student(self, student_id):
        query = "DELETE FROM students WHERE student_id=?"
        database.execute_query(query, (student_id,))

    def search_student(self, search_term):
      
        query = "SELECT * FROM students WHERE name LIKE ? OR student_id = ?"
        rows = database.fetch_query(query, (f"%{search_term}%", search_term))
        return [Student(*row) for row in rows]

    # Reporting Features 

    def get_total_students(self):
        query = "SELECT COUNT(*) FROM students"
        return database.fetch_query(query)[0][0]

    def get_average_grade(self):
        query = "SELECT AVG(grade) FROM students"
        result = database.fetch_query(query)[0][0]
        return result if result else 0.0

    def get_highest_attendance(self):
        query = "SELECT * FROM students ORDER BY attendance DESC LIMIT 1"
        rows = database.fetch_query(query)
        return Student(*rows[0]) if rows else None

    def get_failing_students(self):
        query = "SELECT * FROM students WHERE grade < 50"
        rows = database.fetch_query(query)
        return [Student(*row) for row in rows]

    # Optional Features

    def export_to_csv(self, filename="students.csv"):
        students = self.get_all_students()
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Grade", "Attendance", "Email"])
            for s in students:
                writer.writerow([s.student_id, s.name, s.age, s.grade, s.attendance, s.email])