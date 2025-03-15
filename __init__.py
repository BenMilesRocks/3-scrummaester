import os
from flask import Flask
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if os.path.exists("env.py"):
    import env


#Initialize Flask
app = Flask(__name__)

#Database session variables
engine = create_engine(URI, echo=True)
Session = sessionmaker(engine)
session = Session()
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

#flask_login variables
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
