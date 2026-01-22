class StudentView:

    def show_menu(self):
        print("\nStudent Record Manager")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Show Statistics")
        print("6. Exit")

    def get_input(self, prompt):
        return input(prompt)

    def display_students(self, students):
        for s in students:
            print(s)
