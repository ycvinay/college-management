from person import Person

class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.courses = {}

    def enroll(self, course):
        if course.course_code not in self.courses:
            self.courses[course.course_code] = course
            print(f"Student {self.student_id} enrolled in {course.course_name} successfully!")
        else:
            print(f"Student {self.student_id} is already enrolled in {course.course_name}.")

    def add_grade(self, course_code, grade):
        if course_code in self.courses:
            if 0 <= grade <= 100:
                self.courses[course_code].grade = grade
                print(f"Grade {grade} added for course {course_code}.")
            else:
                print("Grade must be between 0 and 100.")
        else:
            print(f"Course {course_code} not found for student {self.student_id}.")

    def get_grades(self):
        return {course.course_code: {"course_name": course.course_name, "grade": getattr(course, 'grade', None)}
                for course in self.courses.values()}

    def get_details(self):
        details = super().get_details()
        return f"{details}, Student ID: {self.student_id}"
