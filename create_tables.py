from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_number VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_number VARCHAR(20),
    subject VARCHAR(100),
    marks FLOAT,
    FOREIGN KEY (roll_number)
    REFERENCES students(roll_number)
    ON DELETE CASCADE
)
""")

conn.commit()
conn.close()

print("Tables created successfully!")