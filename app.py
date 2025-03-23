import os
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
import bcrypt
from sqlalchemy import update, delete
from __init__ import session, login_manager, app
from models import Team, User, Project, Task
from forms import LoginForm, RegistrationForm
from database import team_db, user_db, project_db, task_db, status
import re

if os.path.exists("env.py"):
    import env

#flask_login - adds route to login page

login_manager.login_view = "login"

#app routing

@login_manager.user_loader
def load_user(username):
    return session.query(User).get(username)

@app.route("/")
def index():
    return render_template("index.html", page_title= "Home")

#error handling

@app.errorhandler(401) 
def not_found(e): 
    return render_template("401.html") 

@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html") 

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
                flash("Successfully Logged In!")
                return redirect(url_for("dashboard"))
            else:
                flash("Incorrect password. Please try again!")
                return render_template("login.html", form=form)
        else:
                flash("Incorrect username. Please try again!")
                return render_template("login.html", form=form)

    return render_template("login.html", page_title= "Login", form = form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Successfully Logged Out!")
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
        flash("New Account Created!")
        return redirect(url_for("login"))

    return render_template("register.html", page_title= "Register", form = form)

#-DASHBOARD

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    user_id = int(current_user.id)
    return render_template("dashboard.html", page_title= "Dashboard", user_id = user_id, task_list = task_db, user_list = user_db)


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
    previous_url = request.referrer

    if request.method == "POST":
        project = Project(
            project_name = request.form.get("project_name"),
            project_status = request.form.get("project_status"),
            team_id = request.form.get("team_id")
        )
        with session:
            session.add(project)
            session.commit()
            flash("Project Created Successfully!")
        return redirect(request.form.get("next"))
    
    return render_template("add_project.html", teams = team_db, previous_url = previous_url)

@app.route("/update_project/<int:project_id>", methods=["GET", "POST"])
@login_required
def update_project(project_id):
    project = session.get(Project, project_id)
    current_project_name = project.project_name
    current_project_status = project.project_status
    current_team_id = project.team_id

    previous_url = request.referrer

    if request.method == "POST":
        project = update(Project).where(Project.project_id == project_id).execution_options(populate_existing=True).values(
            project_name = request.form.get("project_name"),
            project_status = request.form.get("project_status"),
            team_id = request.form.get("team_id")
            )
        session.execute(project)
        session.commit()
        flash("Project Updated Successfully!")
        return redirect(request.form.get("next"))
    
    return render_template(
        "update_project.html", teams = team_db, project_id = project_id, 
        current_project_name = current_project_name, 
        current_project_status = current_project_status, 
        current_team_id = current_team_id,
        previous_url = previous_url,
        status = status)

@app.route("/delete_project/<int:project_id>")
@login_required
def delete_project(project_id):
    previous_url = request.referrer
    project = delete(Project).where(Project.project_id == project_id)
    session.execute(project)
    session.commit()
    flash("Project Deleted Successfully!")
    return redirect(previous_url)

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
    previous_url = request.referrer

    if request.method == "POST":
        team = Team(
            team_lead = request.form.get("team_lead"),
            team_lead_email = request.form.get("team_lead_email")
        )
        with session:
            session.add(team)
            session.commit()
            flash("Team Added Successfully!")
        return redirect(request.form.get("next"))
    return render_template("add_team.html", previous_url = previous_url)

@app.route("/update_team/<int:team_id>", methods=["GET", "POST"])
@login_required
def update_team(team_id):
    team = session.get(Team, team_id)
    current_team_lead = team.team_lead
    current_team_lead_email = team.team_lead_email

    previous_url = request.referrer

    if request.method == "POST":
        team = update(Team).where(Team.team_id == team_id).execution_options(populate_existing=True).values(
            team_lead = request.form.get("team_lead"),
            team_lead_email = request.form.get("team_lead_email")
            )
        session.execute(team)
        session.commit()
        flash("Team Updated Successfully!")
        return redirect(request.form.get("next"))
    return render_template(
        "update_team.html", teams = team_db,
        team_id = team_id, 
        current_team_lead = current_team_lead, 
        current_team_lead_email = current_team_lead_email,
        previous_url = previous_url
        )

@app.route("/delete_team/<int:team_id>")
@login_required
def delete_team(team_id):
    if team_id == 1:
        flash("Cannot delete Team #1. Please edit team details instead.")
    else:
        team = delete(Team).where(Team.team_id == team_id)
        session.execute(team)
        session.commit()
        flash("Team Deleted Successfully!")
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
    current_fname = user.first_name
    current_lname = user.last_name
    current_role = user.team_role
    current_team_id = user.team_id

    previous_url = request.referrer

    if request.method == "POST":
        user = update(User).where(User.id == user_id).execution_options(populate_existing=True).values(
            first_name = request.form.get("first_name"),
            last_name = request.form.get("last_name"),
            team_role = request.form.get("team_role"),
            team_id  = request.form.get("team_id")
            )
        session.execute(user)
        session.commit()
        flash("User Info Updated Successfully!")
        return redirect(request.form.get("next"))
    return render_template(
        "update_user.html", teams = team_db,
        users = user_db, user_id = user_id,
        current_fname = current_fname,
        current_lname = current_lname,
        current_role = current_role,
        previous_url = previous_url,
        current_team_id = current_team_id
        )

@app.route("/update_current_user", methods=["GET", "POST"])
@login_required
def update_current_user():
    user = session.get(User, int(current_user.id))
    current_fname = user.first_name
    current_lname = user.last_name
    current_email = user.email
    current_role = user.team_role
    current_team_id = user.team_id

    previous_url = request.referrer

    if request.method == "POST":
        hashed_password = bcrypt.hashpw(request.form.get("password").encode('utf8'), bcrypt.gensalt())
        user = update(User).where(User.id == int(current_user.id)).execution_options(populate_existing=True).values(
            first_name = request.form.get("first_name"),
            last_name = request.form.get("last_name"),
            email = request.form.get("email"),
            password = hashed_password.decode('utf8'),
            team_role = request.form.get("team_role"),
            team_id  = request.form.get("team_id")
            )
        session.execute(user)
        session.commit()
        flash("User Info Updated Successfully!")
        return redirect(request.form.get("next"))
    return render_template(
        "update_current_user.html",
        teams = team_db, users = user_db,
        current_fname = current_fname,
        current_lname = current_lname,
        current_role = current_role,
        previous_url = previous_url,
        current_email = current_email,
        current_team_id = current_team_id,
        user_id = int(current_user.id)
        )

@app.route("/delete_user/<int:user_id>")
@login_required
def delete_user(user_id):
    if user_id == 1:
        flash("Cannot delete Super User! Please contact your administrator for more information.")
    else:
        user = delete(User).where(User.id == user_id)
        session.execute(user)
        session.commit()
        flash("User Deleted Successfully!")
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
    previous_url = request.referrer

    # Checks regex for textarea
    
    if request.method == "POST":
        if (re.search("^[^\s]+(\s+[^\s]+)*$", request.form.get("task_description"))) == None:
            flash("Task desription can't have whitespace at the beginning or end of the description. Please try again")
            
        # If valid, submit
        else:

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
                flash("Task Created Successfully!")
                if "add_task" in request.form.get("next"):
                    return redirect(url_for("dashboard"))
                else:
                    return redirect(request.form.get("next"))
        
    return render_template("add_task.html", projects = project_db, users = user_db, teams = team_db, previous_url = previous_url)

@app.route("/update_task/<int:task_id>", methods=["GET", "POST"])
@login_required
def update_task(task_id):
    # Pulls existing values
    task = session.get(Task, task_id)
    current_task_name = task.task_name
    current_task_description = task.task_description
    current_task_status = task.task_status
    current_project_id = task.project_id
    current_assigned_user = task.assigned_user

    previous_url = request.referrer

    # Checks Regex for textarea

    if request.method == "POST":
        if (re.search("^[^\s]+(\s+[^\s]+)*$", request.form.get("task_description"))) == None:
            flash("Task desription can't have whitespace at the beginning or end of the description. Please try again")
            
        # If valid, submit
        else:

            task = update(Task).where(Task.task_id == task_id).execution_options(populate_existing=True).values(
                task_name = request.form.get("task_name"),
                task_description = request.form.get("task_description"),
                task_status = request.form.get("task_status"),
                project_id = request.form.get("project_id"),
                assigned_user = request.form.get("assigned_user")
            )
            session.execute(task)
            session.commit()

            if "update_task" in request.form.get("next"):
                return redirect(url_for("dashboard"))
            else:
                return redirect(request.form.get("next"))
    
    return render_template(
        "update_task.html", projects = project_db, 
        users = user_db, task_id = task_id,
        current_task_name = current_task_name,
        current_task_description = current_task_description,
        current_task_status = current_task_status,
        current_project_id = current_project_id,
        current_assigned_user = current_assigned_user,
        previous_url = previous_url,
        status = status)


@app.route("/delete_task/<int:task_id>")
@login_required
def delete_task(task_id):
    task = delete(Task).where(Task.task_id == task_id)
    session.execute(task)
    session.commit()
    previous_url = request.referrer
    flash("Task Deleted Successfully!")
    return redirect(previous_url)

#-RUN APP

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug= os.environ.get("DEBUG"))
