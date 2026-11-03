# Student Result Management System

## Project Overview
The Student Result Management System is a Python-based application that uses SQLite to manage student records, subjects, marks, and academic results.

## Features
- Add new students
- Add subjects with credit hours
- Record student marks
- Display student transcripts
- Calculate student GPA
- Display the top 5 students
- Export student reports to CSV

## Technologies Used
- Python
- SQLite
- SQL
- Pytest

## Project Structure
```text
StudentResultManagement/
│
├── database.py
├── models.py
├── main.py
├── manage_db.db
├── report.csv
└── tests/
    └── test_models.py
```

## How to Run

1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the database file:

```bash
python database.py
```

5. Run the main application:

```bash
python main.py
```

## Running Tests

Install pytest:

```bash
pip install pytest
```

Run the tests:

```bash
python -m pytest tests
```

## Database Tables
The project uses three SQLite tables:

- **Students:** Stores student ID, name, email, and department.
- **Subjects:** Stores subject ID, name, and credit hours.
- **Marks:** Stores student ID, subject ID, and marks.

## Author
Student Project
