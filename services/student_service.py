from storage.file_storage import load_data, save_data
from models.student import Student


class StudentService:

    def get_all_students(self):
        return load_data()

    def add_student(self, student):
        students = load_data()
        students.append(student.to_dict())
        save_data(students)

    def delete_student(self, student_id):
        students = load_data()
        students = [s for s in students if s["student_id"] != student_id]
        save_data(students)

    def update_student(self, student_id, updated_data):
        students = load_data()
        for s in students:
            if s["student_id"] == student_id:
                s.update(updated_data)
        save_data(students)
