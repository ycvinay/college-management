from student import Student
from teacher import Teacher
from course import Course

class CollegeManagementSystem:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.courses = {}

    def add_student(self, student):
        self.students[student.student_id] = student
        print(f"Student {student.name} added successfully!")

    def add_teacher(self, teacher):
        self.teachers[teacher.teacher_id] = teacher
        print(f"Teacher {teacher.name} added successfully!")

    def add_course(self, course):
        self.courses[course.course_code] = course
        print(f"Course {course.name} added successfully!")

    def enroll_student_in_course(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll(course)
            print(f"Student {student_id} enrolled in course {course_code} successfully!")
        else:
            print("Invalid student ID or course code")

    def assign_teacher_to_course(self, teacher_id, course_code):
        if teacher_id in self.teachers and course_code in self.courses:
            teacher = self.teachers[teacher_id]
            course = self.courses[course_code]
            teacher.assign_course(course)
            course.assign_teacher(teacher)
            print(f"Teacher {teacher_id} assigned to course {course_code} successfully!")
        else:
            print("Invalid teacher ID or course code")

    def add_grade_for_student(self, student_id, course_code, grade):
        if student_id in self.students:
            student = self.students[student_id]
            student.add_grade(course_code, grade)
            print(f"Grade {grade} added for student {student_id} in course {course_code}!")
        else:
            print("Student Not found")

    def view_student_grades(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            return student.get_gardes()
        else:
            print("Student Not found")

