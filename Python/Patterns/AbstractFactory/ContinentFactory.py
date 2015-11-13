from abc import ABCMeta, abstractmethod

class ContinentFactory:
    __classmeta__ = ABCMeta

    def CreateHerbivore(self): pass
    def CreateCarnivore(self): pass

