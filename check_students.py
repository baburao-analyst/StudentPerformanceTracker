from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM students")

print(cursor.fetchone())

conn.close()