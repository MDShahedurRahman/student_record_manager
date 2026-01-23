from storage.file_storage import load_data, save_data
from models.student import Student


class StudentService:

    def get_all_students(self):
        return load_data()
