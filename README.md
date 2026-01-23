# Student Record Manager (CLI) — MVC Python Project

A clean, modular **command-line Student Record Management System** built using **MVC (Model–View–Controller) architecture**.  
This project is designed to demonstrate **software engineering best practices, clean architecture, and professional Git commit workflow**.

---

## Project Structure (MVC)

```
student_record_manager/
│
├── main.py
│
├── models/
│   └── student.py
│
├── views/
│   └── student_view.py
│
├── controllers/
│   └── student_controller.py
│
├── services/
│   └── student_service.py
│
├── storage/
│   └── file_storage.py
│
└── utils/
    └── validators.py
```

---

## Features

- Add student records
- View all students
- Update student data
- Delete student records
- Calculate class statistics (average age)
- File-based persistent storage
- MVC architecture for clean separation of concerns

---

## Why MVC Architecture?

- Clean separation of responsibilities
- Highly maintainable code
- Scalable project design
- Industry-standard backend structure

---

## Git Commit Strategy (40 Commits)

Each commit focuses on **one file and one method**, creating a professional development timeline.

### Setup
1. main.py – initialize application entry point  
2. main.py – add main() function  
3. models/student.py – create Student class  
4. models/student.py – implement to_dict() method  

### View Layer
5. views/student_view.py – create StudentView class  
6. views/student_view.py – add show_menu() method  
7. views/student_view.py – add get_input() method  
8. views/student_view.py – add display_students() method  
9. views/student_view.py – add show_message() method  
