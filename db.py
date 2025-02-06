import os
import psycopg
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.orm import sessionmaker, declarative_base

if os.path.exists("env.py"):
    from env import url

#Open database and create base subclasses
db = create_engine(url)
base = declarative_base()


