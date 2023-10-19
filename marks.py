from flask import Flask, render_template
app = Flask(__name__)

@app.route('/h1/<int:score>')
def h1_name(score):
   return render_template('h1.html', marks = score)

if __name__ == '__main__':
   app.run(debug = True)