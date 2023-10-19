from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class employees(db.Model):
   id = db.Column('employee_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200)) 
   pin = db.Column(db.String(10))

   def __init__(self, name, city, addr,pin):
            self.name = name
            self.city = city
            self.addr = addr
            self.pin = pin

@app.route('/')
def show_all():
   return render_template('showall.html', employees = employees.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         employee = employees(request.form['name'], request.form['city'],
          request.form['addr'], request.form['pin'])
         
         db.session.add(employee)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('showall'))
   return render_template('new1.html')

if __name__ == '__main__':
   with app.app_context():
    db.create_all()
   app.run(debug = True)