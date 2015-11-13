from abc import ABCMeta, abstractmethod

class Document:
    """description of class"""
    __metaclass__ = ABCMeta

    def __init__(self):
        self._pages = []
        self.CreatePages()

    def Pages(self): 
        return self._pages

    @abstractmethod
    def CreatePages(self): pass


