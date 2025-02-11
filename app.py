import os
from flask import Flask, render_template, request, flash
from flask_login import LoginManager, UserMixin
import sqlalchemy
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, String, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
if os.path.exists("env.py"):
    from env import SECRET_KEY, url

#Initialize Flask
app = Flask(__name__)
engine = create_engine(url, echo=True)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = url
login = LoginManager()


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer())
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    username: Mapped[str] = mapped_column(String(30), primary_key=True)
    password:  Mapped[str] = mapped_column(String(80))
    email:  Mapped[str] = mapped_column(String(80))
    role:  Mapped[str] = mapped_column(String(80))
    team_id: Mapped[int] = mapped_column(Integer())

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.first_name!r} {self.last_name!r}, username={self.username!r}, email={self.email!r}, role= {self.role!r}, team id={self.team_id!r})"


#create all declared tables from classes
Base.metadata.create_all(engine)

#Route to Login if not logged in, Dashboard if logged in
@app.route("/")
def index():
    return render_template("login.html", page_title= "Login")

@app.route("/index")
def index():
    return render_template("index.html", page_title= "Home")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
