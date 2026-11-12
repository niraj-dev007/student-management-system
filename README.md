# Student Management System (CLI)

A command-line application to manage student records with persistent storage, built with Python.

---

## Features

- **Add Student** - Name validation, age input, course selection from a menu
- **View All Students** - Formatted table with all enrolled students
- **Search by Roll No.** - Instantly find any student's details
- **Delete Student** - Remove a record; roll numbers never reassign (real-world behavior)
- **Persistent Storage** - All data saved in `student.json`, survives app restarts
- **Input Validation** - Handles wrong inputs gracefully with helpful error messages

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/niraj-dev007/student-management-system.git
   ```

2. Navigate to the project folder:
   ```bash
   cd student-management-system
   ```

3. Run the app:
   ```bash
   python main.py
   ```

> No external libraries needed. Uses Python's built-in `json` and `os` modules only.

---

## Available Courses

| # | Course |
|---|--------|
| 1 | Python Programming |
| 2 | Web Development |
| 3 | Data Science |
| 4 | Java Development |
| 5 | Cyber Security |
| 6 | Artificial Intelligence |
| 7 | Digital Marketing |
| 8 | Graphic Designing |
| 9 | Full Stack Development |
| 10 | Cloud Computing |

---

## Tech Stack

- **Language**: Python 3.x
- **Concepts Used**:
  - Functions & Modular Code
  - File I/O (`json.load` / `json.dump`)
  - Error Handling (`try-except`)
  - Input Validation (`while` loops)
  - `os.path` for cross-platform file paths
  - `enumerate()` and `for-else` construct

---

## Project Structure

```
student-management-system/
|
|-- main.py         # Main application file
|-- student.json    # Auto-generated data file (created on first run)
|-- README.md
```

---

## Author

**Niraj** - [GitHub](https://github.com/niraj-dev007)
