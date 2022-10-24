#!/usr/bin/python3
"""
  inheritance in python
"""


def inherits_from(obj, a_class):
    """inheritance """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
