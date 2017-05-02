"""
Singleton pattern...
"""

__author__ = "Andrew Gafiychuk"


class Singleton(object):
    """
    Singleton pattern implementation class.
    For one class instances.
    
    """
    __instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__new__(cls)

        return cls.__instances[cls]