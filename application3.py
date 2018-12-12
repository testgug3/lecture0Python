import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day ==1
    return render_template("index1.html", new_year=new_year)

@app.route("/names")
def names():
    names = ["Alice","Bob","Charlie"]
    return render_template("loop.html", names=names)

@app.route("/more")
def more():
    return render_template("more.html")


@app.route("/myForm")
def myForm():
    return render_template("myForm.html")


@app.route("/myFormResult", methods=["GET","POST"])
def myFormResult():
    #if request method is get do this
    if request.method == "GET":
        return "Please Submit the form Insted."
    #else do this
    else:
        name = request.form.get("name")
        return render_template("myFormResult.html", name = name)
