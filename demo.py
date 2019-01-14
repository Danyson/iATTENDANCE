from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         rn=request.form['rn']
         nm = request.form['nm']
         dept = request.form['dpt']
         sem = request.form['sem']
        
         
         with sql.connect("student.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO student_det (reg_no,name,dept,sem) VALUES (?,?,?,?)",(rn,nm,dept,sem) )
               
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("student.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from student_det")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)
if __name__ == '__main__':
   app.run(debug = True)
