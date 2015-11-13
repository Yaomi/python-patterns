from abc import ABCMeta, abstractmethod
import InvestorBase

class Stock:
    __metaclass__ = ABCMeta

    def __init__(self, symbol:str, price:float):
        self._symbol = symbol
        self._price = price
        self._investors = []

    def Attach(self, investor:InvestorBase):
        self._investors.append(investor)

    def Detach(self, investor:InvestorBase):
        self._investors.remove(investor)

    def Notify(self):
        for investor in self._investors:
            investor.Update(self)

    def GetPrice(self):
        return self._price

    def SetPrice(self, value:float):
        if self._price != value:
            self._price = value
            self.Notify()

    Price = property(GetPrice, SetPrice)
    
    def GetSymbol(self):
        return self._symbol

    Symbol = property(GetSymbol)

