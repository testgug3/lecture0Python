from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/temp")
def temp():
    headline = "Hello Flask Templating!!"
    return render_template("index.html", headline=headline)