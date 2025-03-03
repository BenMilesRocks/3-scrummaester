import os
from flask import render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
import bcrypt
from __init__ import session, login_manager, app
from models import Team, User, Project, Task
from forms import RegistrationForm, LoginForm
from database import (team_db, user_db, project_db, task_db, task_by_project,
                    task_by_user, project_by_team, project_by_user, user_by_project,
                    user_by_team, outstanding_task_by_project, completed_task_by_project,
                    outstanding_task_by_user, completed_task_by_user)



@login_manager.user_loader
def load_user(username):
    return session.query(User).get(username)





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
    return render_template("projects.html", page_title= "Projects", project_list = project_db)

@app.route("/teams", methods=["GET", "POST"])
@login_required
def teams():
    return render_template("teams.html", page_title= "Teams", team_list = team_db)

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
