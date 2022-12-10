import sqlite3

### FUTURE: make a function to insert tasks one-b-one or
### several at the same time.

# Connection Obj is created vi connect method
conn = sqlite3.connect('DB_files/todo_proc.db')

# Create Cursor Obj that allows execute SQL statments in the DB
c = conn.cursor()

# Execute, a cursor method that allow exec one query
c.execute(''' CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    priority INTEGER NOT NULL
);''')

# INSERT INTO statement must be commited - insert only one row 
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
# [ Reminds me map() funct.: itr = map(lambda n: n * n, [1,2,3]) ]

# To close connection w/DB
conn.close()