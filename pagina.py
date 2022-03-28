from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenido a mi página"

@app.route("/hello")
def hello():
    return ""