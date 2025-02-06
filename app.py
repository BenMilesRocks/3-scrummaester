import os
from flask import Flask, render_template, request, flash
from flask_login import LoginManager
if os.path.exists("env.py"):
    from env import postgresql, SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

login = LoginManager()

#Route to Login if not logged in, Dashboard if logged in
@app.route("/")
def index():
    return render_template("login.html", page_title= "Login")

@app.route("/index")
def index():
    return render_template("index.html", page_title= "Home")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
