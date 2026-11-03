import sqlite3

conn = sqlite3.connect("manage_db.db")
cursor = conn.cursor()

cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table'")

for table in cursor.fetchall():
    print(table)
    print()

conn.close()