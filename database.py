from sqlalchemy import select

from __init__ import session
from models import Team, User, Project, Task

team_db = session.query(Team)
user_db = session.query(User)
project_db = session.query(Project)
task_db = session.query(Task)

#Project by Team

def project_by_team(team):
    team_projects = session.query(Project).filter_by(team_id = team)
    for project in team_projects:
        return project

#Task by Project

def task_by_project(project):
    project_tasks = session.query(Task).filter_by(project_id = project).order_by(Task.task_status.desc)
    for task in project_tasks:
        return task
    
def outstanding_task_by_project(project):
    project_tasks = session.query(Task).filter_by(project_id = project).filter_by(task_status = "outstanding")
    for task in project_tasks:
        return task

def completed_task_by_project(project):
    project_tasks = session.query(Task).filter_by(project_id = project).filter_by(task_status = "completed")
    for task in project_tasks:
        return task

#User by Team

def user_by_team(team):
    team_users = session.query(User).filter_by(team_id = team)
    for user in team_users:
        return user
    
#Task by User

def task_by_user(user):
    user_tasks = session.query(Task).filter_by(user_id = user)
    for task in user_tasks:
        return task
    
def outstanding_task_by_user(user):
    user_tasks = session.query(Task).filter_by(user_id = user).filter_by(task_status = "outstanding")
    for task in user_tasks:
        return task
    
def completed_task_by_user(user):
    user_tasks = session.query(Task).filter_by(user_id = user).filter_by(task_status = "completed")
    for task in user_tasks:
        return task

#User by Project

def user_by_project(project):
    project_users = session.query(User).filter_by(project_id = project)
    for user in project_users:
        return user

#Project by User

def project_by_user(user):
    user_projects = session.query(Project).filter_by(user_id = user)
    for project in user_projects:
        return project


#Functions for pulling all data

def all_task_by_project(projects):
    for project in projects:
        return task_by_project(project)