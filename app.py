import os
from flask import Flask, render_template, request, flash
from flask_login import LoginManager, UserMixin
import sqlalchemy
if os.path.exists("env.py"):
    from env import SECRET_KEY, url

#Initialize Flask
app = Flask(__name__)
db = sqlalchemy(app)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = url
login = LoginManager()

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer)
    first_name = db.Column(db.String(20), nullable= False)
    last_name = db.Column(db.String(20), nullable= False)
    username = db.Column(db.String(20), nullable= False, primary_key= True)
    password = db.Column(db.String(80), nullable= False)
    email = db.Column(db.String(50), nullable= False)
    role = db.Column(db.String(20), nullable= False)
    team_id = db.Column(db.Integer, foreign_key= True)

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
