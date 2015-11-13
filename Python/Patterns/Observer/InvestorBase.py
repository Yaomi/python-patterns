from abc import ABCMeta, abstractmethod
import Stock

class InvestorBase(object):
    __metaclass__ = ABCMeta

    def Update(self, stock:Stock): pass


