import os
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, String, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
import bcrypt

if os.path.exists("env.py"):
    from env import SECRET_KEY, url


#Initialize Flask
app = Flask(__name__)
engine = create_engine(url, echo=True)
Session = sessionmaker(engine)
session = Session()


app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = url
login = LoginManager()


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer())
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    username: Mapped[str] = mapped_column(String(30), primary_key=True, unique=True)
    password:  Mapped[str] = mapped_column(String(80))
    email:  Mapped[str] = mapped_column(String(80), unique=True)
    team_role:  Mapped[str] = mapped_column(String(80))
    team_id: Mapped[int] = mapped_column(Integer())

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.first_name!r} {self.last_name!r}, username={self.username!r}, email={self.email!r}, role= {self.role!r}, team id={self.team_id!r})"
    

user_db = session.query(User)

class RegistrationForm(FlaskForm):
    first_name = StringField(validators=[InputRequired(), Length(min=1, max=30)], render_kw={"placeholder":"First Name"})
    last_name = StringField(validators=[InputRequired(), Length(min=1, max=30)], render_kw={"placeholder":"Last Name"})
    username = StringField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"placeholder":"Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"placeholder":"Password"})
    email = StringField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"placeholder":"Email Address"})
    team_role = StringField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"placeholder":"Job Role"})
    team_id = IntegerField(validators=[InputRequired()], render_kw={"placeholder":"Team Number"})

    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_name = session.query(User).filter_by(
            username = username.data).first()
        if existing_user_name:
            raise ValidationError(
                "That username already exists. Please choose a different one"
            )
        

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"placeholder":"Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"placeholder":"Password"})

    submit = SubmitField("Log In")


#create all declared tables from classes
#Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)

#Route to Login if not logged in, Dashboard if logged in
@app.route("/", methods=["GET", "POST"])
def index():
    form = LoginForm()
    return render_template("index.html", page_title= "Login", form = form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.hashpw(form.password.data, bcrypt.gensalt())
        new_user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            password = hashed_password,
            email = form.email.data,
            team_role = form.team_role.data,
            team_id = form.team_id.data)
        session.add(new_user)
        session.commit()
        return redirect(url_for("index"))

    return render_template("register.html", page_title= "Register", form = form)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", page_title= "Dashboard")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
