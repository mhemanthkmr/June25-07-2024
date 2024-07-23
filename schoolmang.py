class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, id, name, age, grade):
        super().__init__(id, name, age)
        self.grade = grade

    def __str__(self):
        return f"Student(ID: {self.id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade})"

class Teacher(Person):
    def __init__(self, id, name, age, subject):
        super().__init__(id, name, age)
        self.subject = subject

    def __str__(self):
        return f"Teacher(ID: {self.id}, Name: {self.name}, Age: {self.age}, Subject: {self.subject})"

class SchoolManagement:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, id, name, age, grade):
        student = Student(id, name, age, grade)
        self.students.append(student)
        print(f"Added {student}")

    def add_teacher(self, id, name, age, subject):
        teacher = Teacher(id, name, age, subject)
        self.teachers.append(teacher)
        print(f"Added {teacher}")

    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(student)

    def view_teachers(self):
        if not self.teachers:
            print("No teachers found.")
        else:
            for teacher in self.teachers:
                print(teacher)

def main():
    school = SchoolManagement()

    while True:
        print("""
        Please select your options below :
            1) Add Student
            2) Add Teacher
            3) View Students
            4) View Teachers
            5) Exit
        """)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("")
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            school.add_student(id, name, age, grade)

        elif choice == 2:
            print("")
            id = int(input("Enter teacher ID: "))
            name = input("Enter teacher name: ")
            age = int(input("Enter teacher age: "))
            subject = input("Enter teacher subject: ")
            school.add_teacher(id, name, age, subject)

        elif choice == 3:
            print("\nStudents List:")
            school.view_students()

        elif choice == 4:
            print("\nTeachers List:")
            school.view_teachers()

        elif choice == 5:
            print("Program Successfully Executed")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
