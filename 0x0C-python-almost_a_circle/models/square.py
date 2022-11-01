!#/usr/bin/python3
"""square"""
from rectangle import Rectangle 


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(def __init__(size, x, y, id)
    
    def __str__(self):
        """returns  shape information"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.height)
