from flask import Flask

app = Flask(__web-application__)

@app.route("/")
def home():
    return "Hello"
