import sqlite3

# Connection Obj is created vi connect method
conn = sqlite3.connect('DB_files/todo_0.db')

# Create Cursor Obj that allows execute SQL statments in the DB
c = conn.cursor()

# Execute, a cursor method that allow exec one query
c.execute(''' CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    priority INTEGER NOT NULL
);''')

# INSERT INTO statement must be commited 
c.execute('INSERT INTO tasks(name, priority) VALUES(?,?)',
('My first task', 1))
conn.commit()

# To INSERT several rows (registers) - executemany() method
ltasks = [
    ('My second task', 5),
    ('My third task', 10),
    ('My fourth task', 12)
]
c.executemany('INSERT INTO tasks(name, priority) VALUES(?,?)', ltasks)
conn.commit()

# modifing DB data - change priority task 1 (UPDATE) - must commit
c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (20, 1))
conn.commit()

# deleting data - DELETE
c.execute('DELETE FROM tasks WHERE id = ?', (1,))
conn.commt()

# read the DB data - Cursor Obj. w/aprop. SELECT is an itarator
for row in c.execute('SELECT * FROM tasks'):
    print(row)

# To close connection w/DB
conn.close()
