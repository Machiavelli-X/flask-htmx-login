from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize session
Session(app)

# 🏠 Default route
@app.route("/")
def index():
    if session.get("logged_in"):
        return render_template("home.html")
    return render_template("index.html")


# 🏠 Home route (explicit)
@app.route("/home")
def home():
    if not session.get("logged_in"):
        return redirect(url_for("index"))
    return render_template("home.html", show_welcome=False)


# 🔐 Login route
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "Demo_user" and password == "pass1234":
        session["logged_in"] = True
        return render_template("home.html", show_welcome=True)
    else:
        return render_template("index.html", error="Invalid username or password!")


# 🚪 Logout route
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/debug")
def debug():
    return {"logged_in": session.get("logged_in")}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
