import os
from flask import Flask, render_template, redirect, url_for
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, Boolean, String, Integer, BigInteger, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
import bcrypt

if os.path.exists("env.py"):
    from env import SECRET_KEY, url


#Initialize Flask
app = Flask(__name__)

#Database session variables
engine = create_engine(url, echo=True)
Session = sessionmaker(engine)
session = Session()
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = url

#flask_login variables
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(username):
    return session.query(User).get(username)

class Base(DeclarativeBase):
    pass

class Team(Base):
    __tablename__ = "teams"

    team_id: Mapped[int] = mapped_column(BigInteger(), autoincrement=True, primary_key=True)
    team_lead: Mapped[str] = mapped_column(String(30))
    team_lead_email: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"Team(Team Id={self.team_id!r}, Team Lead={self.team_lead!r}, Contact Email={self.team_lead_email!r})"
    
class User(UserMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger(), autoincrement=True, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(80), unique=True)
    team_role: Mapped[str] = mapped_column(String(80))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.first_name!r} {self.last_name!r}, username={self.username!r}, email={self.email!r}, role= {self.role!r}, team id={self.team_id!r})"

class Project(Base):
    __tablename__ = "projects"

    project_id: Mapped[int] = mapped_column(BigInteger(), autoincrement=True, primary_key=True)
    project_name: Mapped[str] = mapped_column(String(30))
    project_status: Mapped[str] = mapped_column(String(30))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))

    def __repr__(self) -> str:
        return f"Project(Project Id={self.project_id!r}, Project Name={self.project_name!r}, Status={self.project_status!r}, Team Id={self.team_id!r})"

class Task(Base):
    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(BigInteger(), autoincrement=True, primary_key=True)
    task_name: Mapped[str] = mapped_column(String(50))
    task_description: Mapped[str] = mapped_column(String(3000))
    task_status: Mapped[str] = mapped_column(String(30))
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.project_id"))
    assigned_user: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"Task(Task Id={self.task_id!r}, Task Name={self.task_name!r}, Description={self.task_description!r} Status={self.task_status!r}, Project Id={self.project_id!r}, Assigned User={self.assigned_user!r})"


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


#create values for testing

temp_pass = "password"
hash_password = bcrypt.hashpw(temp_pass.encode('utf8'), bcrypt.gensalt())

team1 = Team(
    team_lead = "Ben Miles",
    team_lead_email = "email@email.com"
)

user1 = User(
    first_name = "Ben",
    last_name = "Miles",
    username = "user1",
    password = hash_password.decode('utf8'),
    email = "email@email.com",
    team_role = "Test Role",
    team_id = 1
)

project1 = Project(
    project_name = "Test Project",
    project_status = "Active",
    team_id = 1
)

task1 = Task(
    task_name = "Test Task",
    task_description = "A task to test the site & database functions",
    task_status = "Active",
    project_id = 1,
    assigned_user = 1
)

#create all declared tables from classes
#Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)


#add data into tables
#session.add(team1)
#session.add(user1)
#session.add(project1)
#session.add(task1)
#session.commit()



@app.route("/")
def index():
    return render_template("index.html", page_title= "Home")

#Route to Login if not logged in, Dashboard if logged in
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = session.query(User).filter_by(
            username = form.username.data).first()
        if user:
            password = user.password.encode('utf8')
            submit_pass = form.password.data.encode('utf8')
            if bcrypt.checkpw(submit_pass, password):
                login_user(user)
                return redirect(url_for("dashboard"))
            else:
                return print("password isn't matching")

    return render_template("login.html", page_title= "Login", form = form)

login_manager.login_view = "User.login"



@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf8'), bcrypt.gensalt())
        new_user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            password = hashed_password.decode('utf8'),
            email = form.email.data,
            team_role = form.team_role.data,
            team_id = form.team_id.data)            
        session.add(new_user)
        session.commit()    
        return redirect(url_for("login"))

    return render_template("register.html", page_title= "Register", form = form)

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template("dashboard.html", page_title= "Dashboard")

@app.route("/projects", methods=["GET", "POST"])
@login_required
def projects():
    return render_template("projects.html", page_title= "Projects")

@app.route("/teams", methods=["GET", "POST"])
@login_required
def teams():
    return render_template("teams.html", page_title= "Teams")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
