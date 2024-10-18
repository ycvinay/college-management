from management_system import CollegeManagementSystem
from teacher import Teacher
from student import Student
from course import Course

college = CollegeManagementSystem()

def add_student():
    try:
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        email = input("Enter student's email: ")
        student_id = input("Enter student's ID: ")
        student = Student(name, age, email, student_id)
        college.add_student(student)
    except ValueError:
        print("Invalid input for age. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_teacher():
    try:
        name = input("Enter teacher's name: ")
        age = int(input("Enter teacher's age: "))
        email = input("Enter teacher's email: ")
        teacher_id = input("Enter teacher's ID: ")
        teacher = Teacher(name, age, email, teacher_id)
        college.add_teacher(teacher)
    except ValueError:
        print("Invalid input for age. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_course():
    try:
        course_code = input("Enter course code: ")
        course_name = input("Enter course name: ")
        course = Course(course_code, course_name)
        college.add_course(course)
    except Exception as e:
        print(f"An error occurred: {e}")

def enroll_student_in_course():
    try:
        student_id = input("Enter student ID: ")
        course_code = input("Enter course code: ")
        college.enroll_student_in_course(student_id, course_code)
    except Exception as e:
        print(f"An error occurred: {e}")

def assign_teacher_to_course():
    try:
        teacher_id = input("Enter teacher ID: ")
        course_code = input("Enter course code: ")
        college.assign_teacher_to_course(teacher_id, course_code)
    except Exception as e:
        print(f"An error occurred: {e}")

def add_grade():
    try:
        student_id = input("Enter student ID: ")
        course_code = input("Enter course code: ")
        grade = int(input("Enter grade: "))
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        college.add_grade_for_student(student_id, course_code, grade)
    except ValueError:
        print("Invalid input for grade. Please enter a number between 0 and 100.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_student_grades():
    try:
        student_id = input("Enter student ID: ")
        grades = college.view_student_grades(student_id)
        if grades:
            print(f"Grades for student {student_id}:")
            for course_code, grade_info in grades.items():
                course = college.courses[course_code]
                teacher_name = course.teacher.name if course.teacher else "No teacher assigned"
                grade = grade_info["grade"]
                print(f"{course.course_name}, Teacher: {teacher_name}, Grade: {grade}")
        else:
            print("No grades found.")
    except Exception as e:
        print(f"An error occurred: {e}")

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
        try:
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
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
