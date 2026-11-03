
import sqlite3
import csv
import os

class StudentManager:

    def __init__(self):
        print(os.path.abspath("manage_db.db"))
        self.conn = sqlite3.connect("manage_db.db")
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()

    def add_student(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        department = input("Enter Department: ")

        self.cursor.execute(
            """INSERT INTO Students(Name,Email,Department)
            VALUES(?,?,?)""",
            (name, email, department)
        )

        self.conn.commit()
        print("Student Added Successfully")

    def add_subject(self):
        name = input("Enter Subject Name: ")
        credit = int(input("Enter Credit Hours: "))

        self.cursor.execute(
            """INSERT INTO Subjects(Name,Credit_Hours)
            VALUES(?,?)""",
            (name, credit)
        )

        self.conn.commit()
        print("Subject Added Successfully")

    def record_marks(self):
        student_id = int(input("Student ID: "))
        subject_id = int(input("Subject ID: "))
        marks = float(input("Marks: "))

        self.cursor.execute(
            """INSERT INTO Marks(Student_id,Subject_id,Marks)
            VALUES(?,?,?)""",
            (student_id, subject_id, marks)
        )

        self.conn.commit()
        print("Marks Recorded Successfully")

    def display_transcript(self):
        student_id = int(input("Enter Student ID: "))

        self.cursor.execute(
            """SELECT s.Name, sub.Name, m.Marks
            FROM Marks m
            JOIN Students s ON s.Student_id = m.Student_id
            JOIN Subjects sub ON sub.Subject_id = m.Subject_id
            WHERE s.Student_id = ?""",
            (student_id,)
        )

        records = self.cursor.fetchall()

        print("Transcript")

        for row in records:
            print(f"Student: {row[0]}")
            print(f"Subject: {row[1]}")
            print(f"Marks: {row[2]}")
            print("----------------")

    def get_grade_point(self, marks):
        if marks >= 85:
            return 4.0
        elif marks >= 75:
            return 3.0
        elif marks >= 65:
            return 2.0
        elif marks >= 50:
            return 1.0
        else:
            return 0.0

    def calculate_gpa(self):
        student_id = int(input("Enter Student ID: "))

        self.cursor.execute(
            """SELECT Marks FROM Marks WHERE Student_id = ?""",
            (student_id,)
        )

        records = self.cursor.fetchall()

        if not records:
            print("No Marks Found")
            return

        total = 0

        for row in records:
            total += self.get_grade_point(row[0])

        gpa = total / len(records)

        print(f"\nGPA = {round(gpa, 2)}")

    def top_students(self):
        self.cursor.execute(
            """SELECT s.Name, AVG(m.Marks)
            FROM Students s
            JOIN Marks m ON s.Student_id = m.Student_id
            GROUP BY s.Student_id
            ORDER BY AVG(m.Marks) DESC
            LIMIT 5"""
        )

        records = self.cursor.fetchall()

        print("\nTop 5 Students\n")

        for i, row in enumerate(records, start=1):
            print(i, row[0], round(row[1], 2))

    def export_csv(self):
        self.cursor.execute(
            """SELECT s.Name, AVG(m.Marks)
            FROM Students s
            JOIN Marks m ON s.Student_id = m.Student_id
            GROUP BY s.Student_id"""
        )

        records = self.cursor.fetchall()

        with open("report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Student Name", "Average Marks"])
            writer.writerows(records)

        print("CSV Exported Successfully")

    def close(self):
        self.conn.close()
