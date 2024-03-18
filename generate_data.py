import sqlite3
import random
from faker import Faker

fake = Faker()

# Connect to the database
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Generate groups
groups = [("Group A",), ("Group B",), ("Group C",)]
cursor.executemany('INSERT INTO groups (name) VALUES (?)', groups)

# Generate teachers
teachers = [(fake.name(),) for _ in range(random.randint(3, 5))]
cursor.executemany('INSERT INTO teachers (name) VALUES (?)', teachers)

# Generate subjects
subject_names = [fake.job() for _ in range(random.randint(5, 8))]
subjects = [(name, random.randint(1, len(teachers))) for name in subject_names]
cursor.executemany('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', subjects)

# Get group IDs
cursor.execute('SELECT id FROM groups')
group_ids = [id[0] for id in cursor.fetchall()]

# Generate students
students = [(fake.name(), random.choice(group_ids)) for _ in range(random.randint(30, 50))]
cursor.executemany('INSERT INTO students (name, group_id) VALUES (?, ?)', students)

# Generate grades
cursor.execute('SELECT id FROM students')
student_ids = [id[0] for id in cursor.fetchall()]

cursor.execute('SELECT id FROM subjects')
subject_ids = [id[0] for id in cursor.fetchall()]

grades = []
for student_id in student_ids:
  for _ in range(random.randint(1, 20)):
    grades.append((student_id, random.choice(subject_ids), random.randint(1, 100), fake.date_between(start_date='-1y', end_date='today')))

cursor.executemany('INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)', grades)

# Save changes and close the connection
conn.commit()
conn.close()
