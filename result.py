from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
   dict = {'phy':65,'che':87,'maths':73}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)