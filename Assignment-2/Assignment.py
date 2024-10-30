import json 

class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nAddress: {self.address}")

class Student(Person):
    def __init__(self, name, age, gender, address, student_id):
        super().__init__(name, age, gender, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        if subject in self.courses:
            self.grades[subject] = grade
            print(f"Grade {grade} for {self.name} in {subject} added successfully.")
        else:
            print(f"{subject} is not a course for {self.name}.")

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course}.")
        else:
            print(f"{self.name} is already enrolled in {course}.")

    def display_student_info(self):
        self.display_person_info()
        print(f"Student ID: {self.student_id}")
        print(f"Enrolled Courses: {', '.join(self.courses) if self.courses else 'None'}")
        print(f"Grades: {self.grades if self.grades else 'No grades assigned'}")
    
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'address': self.address,
            'student_id': self.student_id,
            'grades': self.grades,
            'courses': self.courses
        }

class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student.student_id not in [s.student_id for s in self.students]:
            self.students.append(student)
            student.enroll_course(self.course_name)
        else:
            print(f"Student {student.name} is already enrolled in this course.")

    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor}")
        print("Enrolled Students: ", ", ".join([student.name for student in self.students]) if self.students else "None")
    
    def to_dict(self):
        return {
            'course_name': self.course_name,
            'course_code': self.course_code,
            'instructor': self.instructor,
            'students': [student.student_id for student in self.students]
        }

# Data storage
students = {}
courses = {}

# Save Data Function
def save_data():
    data = {
        'students': {sid: student.to_dict() for sid, student in students.items()},
        'courses': {cid: course.to_dict() for cid, course in courses.items()}
    }
    with open('data.json', 'w') as file:
        json.dump(data, file)
    print("All student and course data saved successfully.")

# Load Data Function
def load_data():
    global students, courses
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            for sid, s_data in data['students'].items():
                student = Student(s_data['name'], s_data['age'], s_data['gender'], s_data['address'], s_data['student_id'])
                student.courses = s_data['courses']
                student.grades = s_data['grades']
                students[sid] = student
            for cid, c_data in data['courses'].items():
                course = Course(c_data['course_name'], c_data['course_code'], c_data['instructor'])
                courses[cid] = course
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found.")

# function with instruction
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    address = input("Enter Address: ")
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists.")
    else:
        student = Student(name, age, gender, address, student_id)
        students[student_id] = student
        print(f"Student {name} (ID: {student_id}) added successfully.")

def add_course():
    course_name = input("Enter Course Name: ")
    course_code = input("Enter Course Code: ")
    instructor = input("Enter Instructor Name: ")
    if course_code in courses:
        print("Course Code already exists.")
    else:
        course = Course(course_name, course_code, instructor)
        courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

def enroll_student_in_course():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    if student_id in students and course_code in courses:
        student = students[student_id]
        course = courses[course_code]
        course.add_student(student)
    else:
        print("Invalid Student ID or Course Code.")

def add_grade_for_student():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    grade = input("Enter Grade: ")
    if student_id in students and course_code in courses:
        student = students[student_id]
        course_name = courses[course_code].course_name
        student.add_grade(course_name, grade)
    else:
        print("Invalid Student ID or Course Code.")

def display_student_details():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        students[student_id].display_student_info()
    else:
        print("Student not found.")

def display_course_details():
    course_code = input("Enter Course Code: ")
    if course_code in courses:
        courses[course_code].display_course_info()
    else:
        print("Course not found.")

# Main Menu Function
def main():
    print('==== Student Management System ====')
    while True:
        print('\n1. Add New Student')
        print('2. Add New Course')
        print('3. Enroll Student in Course')
        print('4. Add Grade for Student')
        print('5. Display Student Details')
        print('6. Display Course Details')
        print('7. Save Data to File')
        print('8. Load Data from File')
        print('0. Exit')
        
        choice = input("Select Option: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            enroll_student_in_course()
        elif choice == '4':
            add_grade_for_student()
        elif choice == '5':
            display_student_details()
        elif choice == '6':
            display_course_details()
        elif choice == '7':
            save_data()
        elif choice == '8':
            load_data()
        elif choice == '0':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
