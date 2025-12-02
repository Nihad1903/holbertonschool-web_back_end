#!/usr/bin/env python3
"""
User Model File
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    '''User Model'''
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    email = Column(String, primary_key = True)
    hashed_password = Column(String, primary_key = True)
    session_id = Column(String, primary_key = True)
    reset_token = Column(String, primary_key = True)    
