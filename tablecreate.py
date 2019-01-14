import sqlite3

conn = sqlite3.connect('student.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE STUDENT_DET
         (REG_NO INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         DEPT            INT     NOT NULL,
         SEM            INT,
         ATTENDANCE         TEXT   );''')
print ("Table created successfully");

conn.close()
