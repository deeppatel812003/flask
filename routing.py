from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
   return 'Hello Deep'
#    app.add_url_rule('/', 'hello', hello_world)

if __name__ == "__main__":
    app.run()

