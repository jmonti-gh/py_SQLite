import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('DB_files/todo_lab1.db')
        self.c = self.conn.cursor()
        self.create_task_tbl()
    
    def create_task_tbl(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority INTEGER NOT NULL
                    );''')

    def add_task(self):
        nm = input('Enter task name: ')
        while nm == '':
            nm = input('Do not enter an empty task name, try again: ')

        find_rslt = self.find_task(nm)
        if find_rslt != None:
            print('That task already exist:', str(find_rslt))
            return "Error: Task exists"

        while True:
            try:
                prty = int(input('Enter priority: '))
                assert prty >= 1
                break
            except (ValueError, AssertionError):
                print('Priority must be an integer greater than 0')

        self.c.execute('INSERT INTO tasks(name, priority) VALUES(?,?)',
         (nm, prty))
        self.conn.commit()

    def find_task(self, name):
        for row in self.c.execute('SELECT * FROM tasks'):
            if name in row:
                return row 

    def add_many_tasks(self):  # Future
        pass

    def show_tasks(self):
        print('{:>4}   {:<25} {:<12}'.format('id', 'task', 'priority'))
        for row in self.c.execute('SELECT * FROM tasks'):
            print('{:>4}   {:<25} {:>4}'.format(row[0], row[1], row[2]))


app = Todo()

r = 'y'
while r[0].lower() == 'y':
    app.add_task()
    r = input('Add another task? ')

# show all tasks in de DB
app.show_tasks()
