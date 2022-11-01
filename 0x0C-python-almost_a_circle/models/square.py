#!/usr/bin/python3
"""square"""
from  models.rectangle import Rectangle 


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the square??? i think"""
        ind = 0
        if args is not None and len(args) != 0:
            for argument in args:
                ind += 1
                if ind == 1:
                    self.id = argument
                elif ind == 2:
                    self.size = argument
                elif ind == 3:
                    self.x = argument
                elif ind == 4:
                    self.y = argument
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """makes a self dictionary"""
        dictionary = {}
        for ind in ["id", "size", "x", "y"]:
            dictionary[ind] = getattr(self, ind)
        return dictionary

    def __str__(self):
        """returns information about the shape"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id,                                                                        self.x,
                self.y,
                self.height
                )
