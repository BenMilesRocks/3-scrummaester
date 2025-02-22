import os
from flask import Flask
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if os.path.exists("env.py"):
    from env import SECRET_KEY, URI


#Initialize Flask
app = Flask(__name__)

#Database session variables
engine = create_engine(URI, echo=True)
Session = sessionmaker(engine)
session = Session()
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = URI

#flask_login variables
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
