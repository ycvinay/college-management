from management_system import CollegeManagementSystem
from teacher import Teacher
from student import Student
from course import Course

college = CollegeManagementSystem()

def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    email = input("Enter student's email: ")
    student_id = input("Enter student's ID: ")
    student = Student(name, age, email, student_id)
    college.add_student(student)

def add_teacher():
    name = input("Enter teacher's name: ")
    age = int(input("Enter teacher's age: "))
    email = input("Enter teacher's email: ")
    teacher_id = input("Enter teacher's ID: ")
    teacher = Teacher(name, age, email, teacher_id)
    college.add_teacher(teacher)

def add_course():
    course_code = input("Enter course code: ")
    course_name = input("Enter course name: ")
    course = Course(course_code, course_name)
    college.add_course(course)

def enroll_student_in_course():
    student_id = input("Enter student ID: ")
    course_code = input("Enter course code: ")
    college.enroll_student_in_course(student_id, course_code)

def assign_teacher_to_course():
    teacher_id = input("Enter teacher ID: ")
    course_code = input("Enter course code: ")
    college.assign_teacher_to_course(teacher_id, course_code)

def add_grade():
    student_id = input("Enter student ID: ")
    course_code = input("Enter course code: ")
    grade = int(input("Enter grade: "))
    college.add_grade_for_student(student_id, course_code, grade)


def view_student_grades(self, student_id):
    if student_id in self.students:
        student = self.students[student_id]
        grades = student.get_grades()

        print(f"Grades for student {student_id}:")
        for course_code, grade_info in grades.items():
            course = self.courses[course_code]
            teacher_name = course.teacher.name if course.teacher else "No teacher assigned"
            grade = grade_info["grade"]
            print(f"{course.course_name}, Teacher: {teacher_name}, Grade: {grade}")
    else:
        print("Student Not found")

def show_menu():
    print("===== College Management System =====")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Add Course")
    print("4. Enroll Student in Course")
    print("5. Assign Teacher to Course")
    print("6. Add Grade for Student")
    print("7. View Student Grades")
    print("8. Exit")
    print("=====================================")


def main():
    while True:
        show_menu()
        choice = int(input("Select an option: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            add_teacher()
        elif choice == 3:
            add_course()
        elif choice == 4:
            enroll_student_in_course()
        elif choice == 5:
            assign_teacher_to_course()
        elif choice == 6:
            add_grade()
        elif choice == 7:
            view_student_grades()
        elif choice == 8:
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.\n")


if __name__ == "__main__":
    main()
