#!/usr/bin/python3

from basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class MedicalHistory(BaseModel):
    
