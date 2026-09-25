#Input functions
students = []
courses = []
marks = {}  
# 1. Input number of students in a class & Input student information (id, name, DoB)
def input_students():
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        print(f"\n Student {i + 1} ---")
        student_id = input("ID student (id): ")
        name = input("Name student (name): ")
        dob = input("Birthday (DoB - dd/mm/yyyy): ")
        
        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }
        students.append(student)

# 2. Input number of courses & Input course information (id, name)
def input_courses():
    num_courses = int(input("\n Number of course: "))
    for i in range(num_courses):
        print(f"\n Course {i + 1} ")
        course_id = input("ID course (id): ")
        name = input("Name course(name): ")
        
        course = {
            "id": course_id,
            "name": name
        }
        courses.append(course)

# 3. Select a course, input marks for student in this course
def input_marks():
    if not courses:
        print("No course is created")
        return
    if not students:
        print("No student is the list!")
        return

    print("\n List of course")
    for course in courses:
        print(f"ID: {course['id']} - Name: {course['name']}")
    
    selected_course_id = input("\n Selected course: ")
    
    if not course_exists:
        print("Courses not existed!")
        return

    print(f"\n Enter the score {selected_course_id} ---")
    for student in students:
        mark = float(input(f" Student score:{student['name']} (ID: {student['id']}): "))
        marks[(student['id'], selected_course_id)] = mark


if __name__ == "__main__":
    input_students()
    input_courses()
    input_marks()
 
#List functions 
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

# 1. List courses
def list_courses():
    print("List of courses")
    for course in courses:
        print(f"ID: {course['id']}, Name course: {course['name']}")

# 2. List students
def list_students():
    print("List of students")
    for student in students:
        print(f"ID: {student['id']}, Student name: {student['name']}")

# 3. Show student marks for a given course
def show_student_marks_for_course(course_id):
    print(f"Student marks {course_id}")
    found = False
    for student in students:
        key = (student["id"], course_id)
        if key in marks:
            print(f"SV: {student['name']} ({student['id']}) - Score: {marks[key]}")
            found = True
    if not found:
        print("Not found course.")


if __name__ == "__main__":
    list_courses()
    print()
    list_students()
    print()
    show_student_marks_for_course("CS101")