
class Student:
    """Represents a single student entity."""
    
    def __init__(self, student_id, name, age, grade, attendance, email=""):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.attendance = attendance
        self.email = email