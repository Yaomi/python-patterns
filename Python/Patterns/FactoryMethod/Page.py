from abc import ABCMeta, abstractmethod

class Page:
    """description of class"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def GetName(self): pass

