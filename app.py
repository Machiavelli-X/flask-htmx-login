from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)#creates the app object
app.secret_key = "supersecretkey"  # required for session to work

@app.route("/")
def index():
    # If user already logged in, show home
    if session.get("logged_in"):
        return render_template("home.html")
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # simple demo login
    if username == "Demo_user" and password == "pass1234":
        session["logged_in"] = True
        return render_template("home.html")
    else:
        # return invalid login message
        return """
        <div class="login-container shake">
          <h1 class="login-title">Welcome Back 👋</h1>
          <p class="login-subtitle" style="color:red;">Invalid credentials!</p>
          <form hx-post="/login" hx-target="body" hx-swap="outerHTML" class="login-form">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit" class="login-btn">Login</button>
          </form>
        </div>
        """

@app.route("/logout")
def logout():
    session.clear()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)#starts the built-in development server
