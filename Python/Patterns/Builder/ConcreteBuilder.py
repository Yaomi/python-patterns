import Builder
import Product

class ConcreteBuilder(Builder.Builder):
    """description of class"""
    _product = Product.Product()

    def BuildPartA(self):
        self._product.Add("PartA")

    def BuildPartB(self):
        self._product.Add("PartB")

    def GetResult(self):
        return self._product

