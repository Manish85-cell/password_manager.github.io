from flask import session ,Flask, redirect, render_template, request
from cs50 import SQL

db = SQL("sqlite:///saved-passwords.db")

app = Flask(__name__)
@app.route("/")
def login():
    return render_template("LOGIN.html")

@app.route("/login", methods=["POST"])
def index():
    return render_template("index.html")

@app.route("/deregister", methods=["POST"])
def deregister():
    site = request.form.get("site")
    if site:
        db.execute("DELETE FROM passwords WHERE site = ?", site)
    return redirect("/passwords")

@app.route("/save", methods=["POST"])
def saver():
    site = request.form.get("site")
    password = request.form.get("password")
    time = request.form.get("time")
    db.execute("INSERT INTO passwords(site, password, time) values(?,?,?)", site, password, time)
    return redirect("/passwords")

@app.route("/passwords")
def passwords():
    site = db.execute("SELECT * FROM passwords")
    return render_template("passwords.html", site=site)
