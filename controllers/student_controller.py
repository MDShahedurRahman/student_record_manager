from views.student_view import StudentView
from services.student_service import StudentService
from models.student import Student
from utils.validators import is_valid_age, is_valid_grade


class StudentController:

    def __init__(self):
        self.view = StudentView()
        self.service = StudentService()

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_input("Choose an option: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                self.show_statistics()
            elif choice == "6":
                break

    def add_student(self):
        sid = self.view.get_input("ID: ")
        name = self.view.get_input("Name: ")
        age = self.view.get_input("Age: ")
        grade = self.view.get_input("Grade: ")

        if not is_valid_age(age) or not is_valid_grade(grade):
            self.view.show_message("Invalid input")
            return

        student = Student(sid, name, int(age), grade)
        self.service.add_student(student)
        self.view.show_message("Student added")
