from abc import ABCMeta, abstractmethod

class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def BuildPartA(self): pass

    @abstractmethod
    def BuildPartB(self): pass

    @abstractmethod
    def GetResult(self): pass


