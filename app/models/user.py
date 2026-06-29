from sqlalchemy import Column, Integer, String
from app.db.session import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Defines the database table  models = database structure  (blueprint for how data is stored)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
