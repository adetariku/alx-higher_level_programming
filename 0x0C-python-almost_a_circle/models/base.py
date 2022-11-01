#!/usr/bin/python3
"""
   unit testing 
   
"""


class Base:
    """ Private instance variable"""

    __nb_objects = 0

    def __init__(self, id = None):
        """class constructor"""
        if not id is None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

