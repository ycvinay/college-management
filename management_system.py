from student import Student
from teacher import Teacher
from course import Course

class CollegeManagementSystem:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.courses = {}

    def add_student(self, student):
        try:
            if student.student_id in self.students:
                raise ValueError(f"Student with ID {student.student_id} already exists.")
            self.students[student.student_id] = student
            print(f"Student {student.name} added successfully!")
        except ValueError as e:
            print(e)

    def add_teacher(self, teacher):
        try:
            if teacher.teacher_id in self.teachers:
                raise ValueError(f"Teacher with ID {teacher.teacher_id} already exists.")
            self.teachers[teacher.teacher_id] = teacher
            print(f"Teacher {teacher.name} added successfully!")
        except ValueError as e:
            print(e)

    def add_course(self, course):
        try:
            if course.course_code in self.courses:
                raise ValueError(f"Course with code {course.course_code} already exists.")
            self.courses[course.course_code] = course
            print(f"Course {course.name} added successfully!")
        except ValueError as e:
            print(e)

    def enroll_student_in_course(self, student_id, course_code):
        try:
            if student_id not in self.students:
                raise KeyError(f"Student with ID {student_id} not found.")
            if course_code not in self.courses:
                raise KeyError(f"Course with code {course_code} not found.")
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll(course)
            print(f"Student {student_id} enrolled in course {course_code} successfully!")
        except KeyError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred while enrolling: {e}")

    def assign_teacher_to_course(self, teacher_id, course_code):
        try:
            if teacher_id not in self.teachers:
                raise KeyError(f"Teacher with ID {teacher_id} not found.")
            if course_code not in self.courses:
                raise KeyError(f"Course with code {course_code} not found.")
            teacher = self.teachers[teacher_id]
            course = self.courses[course_code]
            teacher.assign_course(course)
            course.assign_teacher(teacher)
            print(f"Teacher {teacher_id} assigned to course {course_code} successfully!")
        except KeyError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred while assigning teacher to course: {e}")

    def add_grade_for_student(self, student_id, course_code, grade):
        try:
            if student_id not in self.students:
                raise KeyError(f"Student with ID {student_id} not found.")
            if course_code not in self.courses:
                raise KeyError(f"Course with code {course_code} not found.")
            if not (0 <= grade <= 100):
                raise ValueError("Grade must be between 0 and 100.")
            student = self.students[student_id]
            student.add_grade(course_code, grade)
            print(f"Grade {grade} added for student {student_id} in course {course_code}!")
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred while adding grade: {e}")

    def view_student_grades(self, student_id):
        try:
            if student_id not in self.students:
                raise KeyError(f"Student with ID {student_id} not found.")
            student = self.students[student_id]
            grades = student.get_grades()
            if grades:
                return grades
            else:
                return f"No grades available for student {student_id}."
        except KeyError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred while retrieving grades: {e}")
