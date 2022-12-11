import sqlite3

# Connection Obj is created via connect method
conn = sqlite3.connect('DB_files/todo_0.db')

# Create Cursor Obj that allows execute SQL statments in the DB
c = conn.cursor()

# Cursor Obj. w/apropiate SELECT is treated as iterator
for row in c.execute('SELECT * FROM tasks'):    # note: NO ";"
    print(row)                                  # row in form of a tuple
# [ jm > reminds me file handle Obj.: for ln in open('file', 'r') ]

# Each element of the tuple
for row in c.execute('SELECT * FROM tasks'):   
    print()
    print('id: \t\t', row[0], "  -  ", type(row[0]))
    print('Name: \t\t', row[1], "  -  ", type(row[1]))
    print('Priority: \t', row[2], "  -  ", type(row[2]))

# fetchall method: less efficient cause reads all in memory
print()
c.execute('SELECT * FROM tasks')
lrows = c.fetchall()
print(lrows)                         

# fetchone method: retrieve next available record
print()
c.execute('SELECT * FROM tasks')
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)

# let´s see only one column
print()
v = c.execute('SELECT priority FROM tasks WHERE id = ?', (2,))
print(v)
val = c.fetchone()
print(val)

# To close connection w/DB
conn.close()
