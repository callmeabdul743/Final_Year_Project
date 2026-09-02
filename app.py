from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "fyp-secret-key"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect(url_for("dashboard"))

        else:
            return "Invalid username or password"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)