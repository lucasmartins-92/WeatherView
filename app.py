import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, geocode, weather
import datetime

# Configure application

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database

db = SQL("sqlite:///weather.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # User reached route via POST (as by submitting a form via POST)

    if request.method == "POST":
        # Ensure username was submitted

        if not request.form.get("username"):
            return apology("must provide username", 403)
        # Ensure password was submitted

        elif not request.form.get("password"):
            return apology("must provide password", 403)
        # Query database for username

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)
        # Remember which user has logged in

        session["user_id"] = rows[0]["id"]

        # Redirect user to home page

        user = db.execute(
            "SELECT username FROM users WHERE id = ?",
            session["user_id"],
        )
        return render_template("index.html", user=user[0]["username"])
    # User reached route via GET (as by clicking a link or via redirect)

    else:
        if session:
            user = db.execute(
            "SELECT username FROM users WHERE id = ?",
            session["user_id"],
        )
            return render_template("index.html", user=user[0]["username"])
        else:
            return render_template("login.html")

@app.route("/", methods=["GET"])
def index():
    if session:
        """Show saved locations"""
        saved = db.execute("SELECT * FROM saved WHERE id = ?", session["user_id"])
        user = db.execute(
            "SELECT username FROM users WHERE id = ?",
            session["user_id"],
        )
        if saved == []:
            return render_template("index.html", user=user[0]["username"])
        else:
            return render_template("index.html", user=user[0]["username"], saved=saved)
    else:
        return render_template("index.html", user="user")


@app.route("/search", methods=["POST"])
def search():
    if not request.form.get("search"):
        return apology("please insert place")
    
    lat, lng, formattedaddress = geocode(request.form.get("search"))
    issaved = False

    if session:
        now = datetime.datetime.now()
        testhash = hash(formattedaddress)
        db.execute("INSERT INTO history (id, lat, lng, formattedaddress, moment) VALUES (?, ?, ?, ?, ?)", session["user_id"], lat, lng, formattedaddress, now)
        for row in db.execute("SELECT placehash FROM saved WHERE id = ?", session["user_id"]):
            if row == testhash:
                issaved = True
                break
            else:
                continue

    condition, currenttemp, high, low = weather(lat,lng)
    return render_template("results.html", formattedaddress=formattedaddress, condition=condition.capitalize(), currenttemp=currenttemp, high=high, low=low, lat=lat, lng=lng, issaved=issaved)


@app.route("/saved", methods=["GET", "POST"])
@login_required
def saved():
    if request.method == "GET":
        saved = db.execute("SELECT * FROM saved WHERE id = ?", session["user_id"])
        return render_template("saved.html", saved=saved)
    else:
        savedname = request.form.get("save")
        formattedaddress = request.form.get("formattedaddress")
        placehash = hash(formattedaddress)
        if db.execute("SELECT * FROM saved WHERE placehash = ?", placehash):
            flash("This place was already saved")
            return redirect("/")
        db.execute("INSERT INTO saved (id, savedname, formattedaddress, placehash) VALUES (?, ?, ?, ?)", session["user_id"], savedname, formattedaddress, placehash)
        saved = db.execute("SELECT * FROM saved WHERE id = ?", session["user_id"])
        return render_template("saved.html", saved=saved)
    

@app.route("/history", methods=["GET"])
@login_required
def history():
    if request.method == "GET":
        history = db.execute("SELECT formattedaddress, moment FROM history WHERE id = ? ORDER BY moment DESC LIMIT 10", session["user_id"])
        return render_template("history.html", history=history)


@app.route("/removed", methods=["POST"])
@login_required
def removed():
    placehash = request.form.get("remove")
    db.execute("DELETE FROM saved WHERE placehash = ? AND id = ?", placehash, session["user_id"])
    return redirect("/")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id

    session.clear()

    # Redirect user to login form

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id

    session.clear()

    # User reached route via POST (as by submitting a form via POST)

    if request.method == "POST":
        # Ensure username was submitted

        if not request.form.get("username"):
            return apology("must provide username", 400)
        # Ensure password was submitted

        elif not request.form.get("password"):
            return apology("must provide password", 400)
        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("password confirmation doesn't match", 400)
        # Query database for username

        check = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username doesn't exist

        if len(check) > 0:
            return apology("username already exists", 400)
        # Insert username and hashed password in database

        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            request.form.get("username"),
            generate_password_hash(request.form.get("password")),
        )

        # Remember which user has logged in

        session["user_id"] = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )[0]["id"]

        # Redirect user to home page

        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)

    else:
        return render_template("register.html")
