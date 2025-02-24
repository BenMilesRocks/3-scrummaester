from __init__ import session, login_manager, app
from models import Team, User, Project, Task

team_db = session.query(Team)
user_db = session.query(User)
project_db = session.query(Project)
task_db = session.query(Task)

#Project by Team

def project_by_team(team):
    team_projects = session.query(project_db).filter_by(team_id = team)
    for project in team_projects:
        return project

#Task by Project

def task_by_project(project):
    project_tasks = session.query(task_db).filter_by(project_id = project)
    for task in project_tasks:
        return task

#User by Team

def user_by_team(team):
    team_users = session.query(user_db).filter_by(team_id = team)
    for user in team_users:
        return user
    
#Task by User

def task_by_user(user):
    user_tasks = session.query(task_db).filter_by(user_id = user)
    for task in user_tasks:
        return task

#User by Project

def user_by_project(project):
    project_users = session.query(user_db).filter_by(project_id = project)
    for user in project_users:
        return user

#Project by User

def project_by_user(user):
    user_projects = session.query(project_db).filter_by(user_id = user)
    for project in user_projects:
        return project
    
    