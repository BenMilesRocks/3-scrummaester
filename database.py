from __init__ import session, login_manager, app
from models import Team, User, Project, Task

team_db = session.query(Team)
user_db = session.query(User)
project_db = session.query(Project)
task_db = session.query(Task)