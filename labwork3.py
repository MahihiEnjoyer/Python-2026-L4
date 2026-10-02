#Information from 1b:
courses = [
    {"id": "CS101", "name": "Advanced Python"},
    {"id": "CS102", "name": "Data C"}
]

students = [
    {"id": "SV01", "name": "A"},
    {"id": "SV02", "name": "B"}
]


marks = {
    ("SV01", "CS101"): 8.5,
    ("SV02", "CS101"): 9.0,
    ("SV01", "CS102"): 7.5
}
import math
import numpy as np
#Course class:
class Course:
    def __init__(self, name, credit, mark):
        self.name = name
        self.credit = credit
        self.mark = math.floor(mark * 10) / 10
#Student class:
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []
        self.gpa = 0

    def add_course(self, course):
        self.courses.append(course)
#Calculate GPA:
    def calculate_gpa(self):
        if len(self.courses) == 0:
            self.gpa = 0
            return
        credits = np.array([course.credit for course in self.courses] )
        marks = np.array([course.mark for course in self.courses] )
        self.gpa = np.sum(credits * marks) / np.sum(credits)
        self.gpa = math.floor(self.gpa * 10) / 10

    def display(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)
        print("\nCourses:")
        for course in self.courses:
            print(
                f"  {course.name:<20}"
                f" Credit: {course.credit}"
                f" Mark: {course.mark:.1f}"
            )

        print(f"\nGPA: {self.gpa:.1f}")
#Input student:
def input_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    student = Student(student_id, name)
    number_of_courses = int(input("Enter number of courses: "))
    for i in range(number_of_courses):
        print(f"\nCourse {i + 1}")
        course_name = input("Course name: ")
        credit = float(input("Credit: "))
        mark = float(input("Mark: "))
        course = Course(
            course_name,
            credit,
            mark
        )
        student.add_course(course)
    student.calculate_gpa()
    return student
#Main program:
students = []
print("******************************************")
print("     STUDENT GPA MANAGEMENT SYSTEM")
print("******************************************")
number_of_students = int(input("\nEnter number of students: "))
# Input students:
for i in range(number_of_students):
    print(f"\n*********** STUDENT {i + 1} ************")
    student = input_student()
    students.append(student)
#List:
print("\n\n*******************************************")
print("          ORIGINAL STUDENT LIST")
print("***********************************************")
for student in students:
    student.display()
#Sort by GPA:
students.sort(
    key=lambda student: student.gpa,
    reverse=True
)
#Sorted list:
print("\n\n****************************************")
print("       STUDENTS SORTED BY GPA")
print("             (DESCENDING)")
print("********************************************")
print(
    f"{'Rank':<6}"
    f"{'ID':<15}"
    f"{'Name':<25}"
    f"{'GPA':<6}"
)
print("-" * 52)
for i, student in enumerate(students):
    print(
        f"{i + 1:<6}"
        f"{student.student_id:<15}"
        f"{student.name:<25}"
        f"{student.gpa:<6.1f}"
    )