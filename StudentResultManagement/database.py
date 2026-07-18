import sqlite3

conn = sqlite3.connect("manage_db.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    Student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE,
    Department TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Subjects(
    Subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Credit_Hours INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Marks(
    Marks_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Student_id INTEGER,
    Subject_id INTEGER,
    Marks REAL,

    FOREIGN KEY(Student_id)
    REFERENCES Students(Student_id),

    FOREIGN KEY(Subject_id)
    REFERENCES Subjects(Subject_id)
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")