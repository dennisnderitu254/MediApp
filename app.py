from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, session, redirect, url_for, request
from models.user_model import User
from models.basemodel import BaseModel


Base = declarative_base()

engine = create_engine("mysql://root:root1234@localhost/mediappDATABASE")
Base.metadata.create_all(bind=engine)

# p1 = User("dennis@gmail.com", "Dennis", "Nderitu", "pass1234", "Patient")

# session.add(p1)
# session.commit()
