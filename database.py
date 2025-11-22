import sqlite3
connection=sqlite3.connect('feedback.db')
cursor=connection.cursor()
cmd="""
CREATE TABLE IF NOT EXISTS feedback (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
fullname text not null,
usn varchar(10) not null,
contact varchar(10) not null,
email text not null,
message text not null
)
"""
cursor.execute(cmd)
connection.commit()
cmd="INSERT INTO feedback (fullname, usn,contact, email, message) VALUES (?, ?, ?, ?, ?)"
#cursor.execute(cmd, ('Poorvika', '4mw23ad027', '7022124616', 'poorvika.23ad027@sode-edu,in', 'Great Experience'))
connection.commit()
f=cursor.execute("SELECT * FROM feedback").fetchall()
print(f)
connection.close()


 