from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = 'admin'

@app.route('/')
def index3():
   return render_template('index3.html')

@app.route('/log-in', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('index3'))
			
   return render_template('log-in.html', error = error)

if __name__ == "__main__":
   app.run(debug = True)