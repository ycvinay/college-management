class Course:
    def __init__(self, course_code, name, teacher=None):
        self.course_code = course_code
        self.name = name
        self.teacher = teacher
        self.grade  =None

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def __str__(self):
        return f"{self.course_code}: {self.name}, Teacher: {self.teacher.name if self.teacher else 'None'}, {self.grade if self.grade else 'Not graded'}"
