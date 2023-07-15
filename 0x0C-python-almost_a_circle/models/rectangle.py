#!/usr/bin/python3
"""a rectangle class that inherits from a class Base"""


import json
from models.base import Base


class Rectangle(Base):
    """defines a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize width, height of Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

