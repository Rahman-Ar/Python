#Database Interaction
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Commit changes and close the connection
conn.commit()

cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))

conn.commit()

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute('''
UPDATE users SET age = ? WHERE name = ?
''', (31, 'Alice'))

conn.commit()

cursor.execute('''
DELETE FROM users WHERE name = ?
''', ('Alice',))

conn.commit()

conn.close()
