from sqlalchemy import ForeignKey, String, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass


class Team(Base):
    __tablename__ = "teams"

    team_id: Mapped[int] = mapped_column(
            BigInteger(), autoincrement=True, primary_key=True
        )
    team_lead: Mapped[str] = mapped_column(String(30))
    team_lead_email: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"""Team(Team Id={self.team_id!r}, 
        Team Lead={self.team_lead!r}, 
        Contact Email={self.team_lead_email!r})"""


class User(UserMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
            BigInteger(), autoincrement=True, primary_key=True
        )
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(80), unique=True)
    team_role: Mapped[str] = mapped_column(String(80))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))

    def __repr__(self) -> str:
        return f"""User(id={self.id!r}, 
        name={self.first_name!r} {self.last_name!r}, 
        username={self.username!r}, email={self.email!r}, 
        role= {self.role!r}, team id={self.team_id!r})"""


class Project(Base):
    __tablename__ = "projects"

    project_id: Mapped[int] = mapped_column(
            BigInteger(), autoincrement=True, primary_key=True
        )
    project_name: Mapped[str] = mapped_column(String(30))
    project_status: Mapped[str] = mapped_column(String(30))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))

    def __repr__(self) -> str:
        return f"""Project(Project Id={self.project_id!r}, 
        Project Name={self.project_name!r}, 
        Status={self.project_status!r}, Team Id={self.team_id!r})"""


class Task(Base):
    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(
        BigInteger(), autoincrement=True, primary_key=True
        )
    task_name: Mapped[str] = mapped_column(String(50))
    task_description: Mapped[str] = mapped_column(String(3000))
    task_status: Mapped[str] = mapped_column(String(30))
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.project_id"))
    assigned_user: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"""Task(Task Id={self.task_id!r}, 
        Task Name={self.task_name!r}, 
        Description={self.task_description!r} Status={self.task_status!r}, 
        Project Id={self.project_id!r}, Assigned User={self.assigned_user!r})"""
