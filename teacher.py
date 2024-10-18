from person import Person

class Teacher(Person):
    def __init__(self, name, age, email, teacher_id):
        super().__init__(name, age, email)
        self.teacher_id = teacher_id
        self.courses = []

    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"Course {course.course_name} assigned to teacher {self.teacher_id} successfully!")
        else:
            print(f"Course {course.course_name} is already assigned to teacher {self.teacher_id}.")

    def get_assigned_courses(self):
        if self.courses:
            return [course.course_name for course in self.courses]
        else:
            return "No courses assigned."

    def get_details(self):
        details = super().get_details()
        return f"{details}, Teacher ID: {self.teacher_id}"
