import sqlite3

conn = sqlite3.connect('student.db')
reg_no=input("enter the register number")


name=input("enter the name")
dept=input("enter the department")
sem=input("enter the semester")




conn.execute("insert into STUDENT_DET (reg_no,name,dept, sem) values (?, ?,?, ?)",
            (reg_no,name,dept, sem))
conn.commit()
conn.close()
