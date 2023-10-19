from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def addnew():
    return render_template('student.html')


@app.route('/addrec', methods=['GET', 'POST'])
def addrec():
    msg = ''
    if request.method == 'POST':
        try:
            name = request.form['nm']
            addr = request.form['addr']
            city = request.form['city']
            pincode = request.form['pin']

            print("Name:", name)
            print("Address:", addr)
            print("City:", city)
            print("Pincode:", pincode)

            with sql.connect('database.db') as con:
                cur = con.cursor()
                cur.execute('INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)', (name, addr, city, pincode))
                con.commit()
                msg = 'Data inserted successfully'
        except Exception as e:
            print("Error:", e)
            con.rollback()
            msg = 'Error in insertion operation'

        finally:
            con.close()
            return render_template('result.html', msg=msg)


@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)