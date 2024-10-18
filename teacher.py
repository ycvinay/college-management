from person import Person


class Teacher(Person):
    def __init__(self, name, age, email, teacher_id):
        super().__init__(name, age, email)
        self.teacher_id = teacher_id
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def get_assigned_courses(self):
        return [course.name for course in self.courses]

    def get_details(self):
        details = super().get_details()
        return f"{details}, Teacher ID: {self.teacher_id}"