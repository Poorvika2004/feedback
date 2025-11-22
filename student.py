import sqlite3
connection=sqlite3.connect('student.db')
cursor=connection.cursor()
cmd="""
CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
branch text not null,
usn varchar(10) not null,
cgpa double not null,
sem integer not null
)
"""
cursor.execute(cmd)
connection.commit()
cmd="INSERT INTO student (branch, usn,cgpa, sem) VALUES (?, ?, ?, ?)"
#cursor.execute(cmd, ('AIDS', '4mw23ad027', 8.1, 5))
connection.commit()
f=cursor.execute("SELECT * FROM student").fetchall()
print(f)
r=cursor.execute("SELECT * FROM student WHERE branch=? & usn=?",('AIDS','4mw23ad042',)).fetchall()
print(r)
connection.close()


 