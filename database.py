from sqlalchemy import select

from __init__ import session
from models import Team, User, Project, Task

# All data from table, for iteration in Flask

team_db = session.query(Team)
user_db = session.query(User)
project_db = session.query(Project)
task_db = session.query(Task)

# Tupple for project and task status

status = ("Active", "Completed")