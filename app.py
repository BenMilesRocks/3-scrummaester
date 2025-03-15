import os
from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
import bcrypt
from sqlalchemy import update, delete
from __init__ import session, login_manager, app
from models import Team, User, Project, Task
from forms import LoginForm, RegistrationForm
from database import (team_db, user_db, project_db, task_db)

if os.path.exists("env.py"):
    import env

login_manager.login_view = "User.login"

#app routing

@login_manager.user_loader
def load_user(username):
    return session.query(User).get(username)

@app.route("/")
def index():
    return render_template("index.html", page_title= "Home")

#-LOGIN

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

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

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
            team_id = form.team_id.data.team_id)            
        session.add(new_user)
        session.commit()    
        return redirect(url_for("login"))

    return render_template("register.html", page_title= "Register", form = form)

#-DASHBOARD

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    user_id = int(current_user.id)
    return render_template("dashboard.html", page_title= "Dashboard", user_id = user_id, task_list = task_db)


#-PROJECTS

@app.route("/projects", methods=["GET", "POST"])
@login_required
def projects():
    return render_template(
        "projects.html",
        page_title= "Projects",
        project_list = project_db,
        task_list = task_db,
        team_list = team_db,
        user_list = user_db)

#----------Project CRUD Functions

@app.route("/add_project", methods=["GET", "POST"])
@login_required
def add_project():
    if request.method == "POST":
        project = Project(
            project_name = request.form.get("project_name"),
            project_status = request.form.get("project_status"),
            team_id = request.form.get("team_id")
        )
        with session:
            session.add(project)
            session.commit()
        return redirect(url_for("projects"))
    return render_template("add_project.html", teams = team_db)

@app.route("/update_project/<int:project_id>", methods=["GET", "POST"])
@login_required
def update_project(project_id):
    project = session.get(Project, project_id)

    if request.method == "POST":
        project = update(Project).where(Project.project_id == project_id).execution_options(populate_existing=True).values(
            project_name = request.form.get("project_name"),
            project_status = request.form.get("project_status"),
            team_id = request.form.get("team_id")
            )
        session.execute(project)
        session.commit()
        return redirect(url_for("projects"))
    return render_template("update_project.html", teams = team_db, project_id = project_id)

@app.route("/delete_project/<int:project_id>")
@login_required
def delete_project(project_id):
    project = delete(Project).where(Project.project_id == project_id)
    session.execute(project)
    session.commit()
    return redirect(url_for("projects"))

#-TEAMS

@app.route("/teams", methods=["GET", "POST"])
@login_required
def teams():
    return render_template(
        "teams.html", 
        page_title= "Teams", 
        team_list = team_db, 
        project_list = project_db, 
        task_list = task_db, 
        user_list = user_db
        )

#----------Team CRUD Functions

@app.route("/add_team", methods=["GET", "POST"])
@login_required
def add_team():
    if request.method == "POST":
        team = Team(
            team_lead = request.form.get("team_lead"),
            team_lead_email = request.form.get("team_lead_email")
        )
        with session:
            session.add(team)
            session.commit()
        return redirect(url_for("teams"))
    return render_template("add_team.html")

@app.route("/update_team/<int:team_id>", methods=["GET", "POST"])
@login_required
def update_team(team_id):
    team = session.get(Team, team_id)

    if request.method == "POST":
        team = update(Team).where(Team.team_id == team_id).execution_options(populate_existing=True).values(
            team_lead = request.form.get("team_lead"),
            team_lead_email = request.form.get("team_lead_email")
            )
        session.execute(team)
        session.commit()
        return redirect(url_for("teams"))
    return render_template("update_team.html", teams = team_db, team_id = team_id)

@app.route("/delete_team/<int:team_id>")
@login_required
def delete_team(team_id):
    team = delete(Team).where(Team.team_id == team_id)
    session.execute(team)
    session.commit()
    return redirect(url_for("teams"))

#-USERS

@app.route("/users", methods=["GET", "POST"])
@login_required
def users():
    return render_template(
        "users.html", 
        page_title= "Users",
        team_list = team_db, 
        project_list = project_db, 
        task_list = task_db, 
        user_list = user_db
        )

#----------User CRUD Functions

@app.route("/update_user/<int:user_id>", methods=["GET", "POST"])
@login_required
def update_user(user_id):
    user = session.get(User, user_id)

    if request.method == "POST":
        user = update(User).where(User.id == user_id).execution_options(populate_existing=True).values(
            first_name = request.form.get("first_name"),
            last_name = request.form.get("last_name"),
            email = request.form.get("email"),
            team_role = request.form.get("team_role"),
            team_id  = request.form.get("team_id")
            )
        session.execute(user)
        session.commit()
        return redirect(url_for("users"))
    return render_template("update_user.html", teams = team_db, users = user_db, user_id = user_id)

@app.route("/delete_user/<int:user_id>")
@login_required
def delete_user(user_id):
    user = delete(User).where(User.id == user_id)
    session.execute(user)
    session.commit()
    return redirect(url_for("users"))

#-TASKS

@app.route("/tasks", methods=["GET", "POST"])
@login_required
def tasks():
    return render_template(
        "tasks.html", 
        page_title= "Tasks", 
        team_list = team_db, 
        project_list = project_db, 
        task_list = task_db, 
        user_list = user_db
        )

#----------Task CRUD Functions

@app.route("/add_task", methods=["GET", "POST"])
@login_required
def add_task():
    if request.method == "POST":
        task = Task(
            task_name = request.form.get("task_name"),
            task_description = request.form.get("task_description"),
            task_status = request.form.get("task_status"),
            project_id = request.form.get("project_id"),
            assigned_user = request.form.get("assigned_user")
        )
        with session:
            session.add(task)
            session.commit()
        return redirect(url_for("tasks"))
    return render_template("add_task.html", projects = project_db, users = user_db)

@app.route("/update_task/<int:task_id>", methods=["GET", "POST"])
@login_required
def update_task(task_id):
    task = session.get(Task, task_id)

    if request.method == "POST":
        task = update(Task).where(Task.task_id == task_id).execution_options(populate_existing=True).values(
            task_name = request.form.get("task_name"),
            task_description = request.form.get("task_description"),
            task_status = request.form.get("task_status"),
            project_id = request.form.get("project_id"),
            assigned_user  = request.form.get("assigned_user")
            )
        session.execute(task)
        session.commit()
        return redirect(url_for("tasks"))
    return render_template("update_task.html", projects = project_db, users = user_db, task_id = task_id)


@app.route("/delete_task/<int:task_id>")
@login_required
def delete_task(task_id):
    task = delete(Task).where(Task.task_id == task_id)
    session.execute(task)
    session.commit()
    return redirect(url_for("tasks"))

#-RUN APP

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug= os.environ.get("DEBUG"))
