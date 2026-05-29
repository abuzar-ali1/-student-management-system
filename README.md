# Student Management System (SMS)

A complete Python-based Student Management System handling CRUD operations, data validation, and automated reporting. Data is persistently stored using SQLite. 

## Features
- **CRUD Operations**: Add, view, update, and delete students.
- **Reporting**: View total students, average grades, highest attendance, and failing student records.
- **Persistent Storage**: Uses a local SQLite Database (`students.db`).
- **Data Validation**: Prevents system crashes by strictly validating data types and ranges (e.g., 0-100 for grades).
- **Extra Features**: Search by ID/Name, sort records, and export everything directly to a CSV file.

## Setup Instructions
1. Ensure Python 3.x is installed on your system.
2. Ensure all files (`main.py`, `student.py`, `operations.py`, `database.py`) are in the same directory.
3. No external dependencies are required (Built-in `sqlite3` and `csv` modules are used).

## How to Run
Open your terminal or command prompt, navigate to the project directory, and run:
`python main.py`