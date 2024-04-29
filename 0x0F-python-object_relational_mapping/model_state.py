#!/usr/bin/python3
"""Lists states"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_city import City

Base = declarative_base()


class State(Base):
    """Table representing the states."""
    # Table name
    __tablename__ = 'states'

    # Columns of the table
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)  # Primary key
    name = Column(String(128), nullable=False)  # State name
