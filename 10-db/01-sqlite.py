import sqlite3

# connection = sqlite3.connect("example.db")
connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

cursor.execute("CREATE TABLE tasks (text, is_done)")

tasks = [
    ('Learn Python', True),
    ('Look for a job', False),
    ('Forget everything', False),
]

cursor.executemany("""
INSERT INTO tasks
VALUES (?, ?)
""", tasks)

cursor.execute("""
SELECT *
FROM tasks
WHERE is_done = ?
""", (True,))

for row in cursor:
    print(f"text: {row[0]}, is_done: {row[1]}")

cursor.execute("""
UPDATE tasks
SET is_done = ?
WHERE text = ?
""", (False, 'Learn Python'))

cursor.execute("""
SELECT *
FROM tasks
""")

for row in cursor:
    print(f"text: {row[0]}, is_done: {row[1]}")

connection.close()
