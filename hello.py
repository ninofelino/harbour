from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "FLASK_APP=hello.py flask run"

@app.route("/help")
def help():
    return render_template('views/index.html')   
    