import sqlite3

class Todo:
    def __init__(self):
        # Connection Obj is created via connect method
        self.conn = sqlite3.connect('DB_files/todo_oop.db')
        # Create Cursor Obj: allows execute SQL statments in the DB
        self.c = self.conn.cursor()
        self.create_task_tbl()
    
    def create_task_tbl(self):
        # Execute, a cursor method that allow exec one query
        self.c.execute(''' CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority INTEGER NOT NULL
                    );''')

    def add_task(self):
        nm = input('Enter task name: ')
        prty = int(input('Enter priority: '))
        self.c.execute('INSERT INTO tasks(name, priority) VALUES(?,?)',
         (nm, prty))
        self.conn.commit()

app = Todo()
app.add_task()