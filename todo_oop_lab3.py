''' Future: make an app w/JOINs and w/agregations funct
like CONT or MIN, for example a:
Number Guessing Game w/ history '''

import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('DB_files/todo_lab2.db')
        self.c = self.conn.cursor()
        self.create_task_tbl()
    
    def create_task_tbl(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority INTEGER NOT NULL
                    );''')

    def __inp_priority(sel):
        while True:
            try:
                priority = int(input('Enter priority: '))
                assert priority >= 1
                break
            except (ValueError, AssertionError):
                print('Priority must be an integer greater than 0')
        return priority

    def add_task(self):
        nm = input('Enter task name: ')
        while nm == '':
            nm = input('Do not enter an empty task name, try again: ')

        find_rslt = self.find_task(nm)
        if find_rslt:
            print('That task already exist:', find_rslt)
            return "Error: Task exists"

        prty = self.__inp_priority()

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
        print()
        print('{:>4}   {:<35} {:<12}'.format('id', 'task', 'priority'))
        print(' ' + '-' * 50)
        for row in self.c.execute('SELECT * FROM tasks'):
            print('{:>4}   {:<35} {:>4}'.format(row[0], row[1], row[2]))

    def __find_id(self):
        while True:
            try:
                i_id = int(input('Enter task id: '))
                assert i_id >= 1
                break
            except (ValueError, AssertionError):
                print('id must be an integer greater than 0')
        self.c.execute('SELECT id FROM tasks WHERE id = ?', (i_id,))
        e_id = self.c.fetchone()
        if e_id:
            return e_id[0]

    def change_priority(self):
        id = self.__find_id()
        if id:
            prty = self.__inp_priority()
            self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?', 
            (prty, id))
            self.conn.commit()
        else:
            print('There is no task with that id')

    def delete_task(self):
        id = self.__find_id()
        if id:
            self.c.execute('DELETE FROM tasks WHERE id = ?', (id,))
            self.conn.commit()
        else:
            print('There is no task with that id')

### main
print('\n~~~ Todo List ~~~')

app = Todo()

menu = {
    1 : 'Show Tasks.',
    2 : 'Add Tasks.',
    3 : 'Change Priority.',   
    4 : 'Delete Task.',
    5 : 'Exit.'
}
while True:
    print()
    for k  in sorted(menu):
        print(k, ' -  ', menu[k], sep='')
    option = input('Please select: ')
    if option == '1':
        app.show_tasks()
    elif option == '2':
        app.add_task()
    elif option == '3':
        app.change_priority()
    elif option == '4':
        app.delete_task()
    elif option == '5':
        break
    else:
        print('Invalid option')
