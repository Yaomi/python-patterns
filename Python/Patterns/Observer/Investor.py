import InvestorBase
import Stock

class Investor(InvestorBase.InvestorBase):
    def __init__(self, name:str):
        self._name = name

    def Update(self, stock:Stock):
        print("Notified {0} of {1}'s change to {2}".format(self._name, stock.Symbol, stock.Price))
    
    def GetStock(self):
        return self.Stock

    def SetStock(self, value:Stock):
        self.Stock = value

    Stock = property(GetStock, SetStock)