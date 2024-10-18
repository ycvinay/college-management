from person import Person


class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.courses = {}

    def enroll(self, course):
        self.courses[course.course_code] = course

    def add_grade(self, course_code, grade):
        if course_code in self.courses:
            self.courses[course_code].grade = grade


    def get_gardes(self):
        return {course: course.grade for course in self.courses.values()}

    def get_details(self):
        details = super().get_details()
        return f"{details}, Student ID: {self.student_id}"

